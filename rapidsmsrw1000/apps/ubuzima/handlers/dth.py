#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


##DJANGO LIBRARY
from django.utils.translation import ugettext as _
from django.utils.translation import activate, get_language
from decimal import *
from exceptions import Exception
import traceback
from datetime import *
from time import *
from django.db.models import Q

###DEVELOPED APPS
from rapidsmsrw1000.apps.ubuzima.reports.utils import *
from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from novahandlers import *

DEATH_CODE_PATTERN = "md|nd|cd"
DEATH_LOCATION_PATTERN = "ho|cl|hp|or"

DEATH_CODE = {'md': 'Maternal Death', 'nd': 'Newborn Death', 'cd': 'Child Death'}
DEATH_LOCATION = {'ho': 'At Home', 'cl': 'At Clinic', 'hp': 'At Hospital', 'or': 'On Route'}
CHILD_DEATH_SMS_INDEXES = {'keyword' : 0, 'mother': 1, 'child_number': 2, 'date_of_birth': 3, 'location': 4, 'death_code': 5}
WOMAN_DEATH_SMS_INDEXES = {'keyword' : 0, 'mother': 1, 'location': 2, 'death_code': 3}


def get_date(text):
    """Tries to parse a string into some python date object."""
    
    today = date.today()
    cycle_s = today - timedelta(days = 1000)
    cycle_e = today + timedelta(days = 1000)
       
    date_string = re.search("\s([0-9.]+)\s", text)   
    # full date: DD.MM.YYYY
    if date_string:
        date_pattern = re.search("^(\d+)\.(\d+)\.(\d+)$", date_string.group(1)) 
        if date_pattern:
            dd = date_pattern.group(1)
            mm = date_pattern.group(2)
            yyyy = date_pattern.group(3)
        
            #print "%s = '%s' '%s' '%s'" % (date_string, dd, mm, yyyy)
        
            # make sure we are in the right format
            if len(dd) > 2 or len(mm) > 2 or len(yyyy) != 4: 
                raise Exception(_("Invalid date format, must be in the form: DD.MM.YYYY"))
            
            # invalid year
            if int(yyyy) > cycle_e.year or int(yyyy) < cycle_s.year:
                raise Exception(_("Invalid year, year must be between %(year_start)d and %(year_end)d, and date in the form: DD.MM.YYYY" % { 'year_start': cycle_s.year, 'year_end': cycle_e.year}))
        
            # invalid month
            if int(mm) > 12 or int(mm) < 1:
                raise Exception(_("Invalid month, month must be between 1 and 12, and date in the form: DD.MM.YYYY"))
        
            # invalid day
            if int(dd) > 31 or int(dd) < 1:
                raise Exception(_("Invalid day, day must be between 1 and 31, and date in the form: DD.MM.YYYY"))
        
        
            #Otherwise, parse into our date format
            return date(int(yyyy), int(mm), int(dd))
        else:
            raise Exception(_("Invalid date format, must be in the form: DD.MM.YYYY"))
    else:
        raise Exception(_("Invalid date format, must be in the form: DD.MM.YYYY"))    


class DeathRecord(object):
    """
    The Death report has to be parsed at receipt of the raw SMS and
    Its content has to be parsed and instantiate in this object.
    """
        
    def __init__(self, raw_sms):
        self.raw_text = raw_sms
        self.mother = None
        self.child_number = None
        self.date_of_birth = None
        self.location = None
        self.death_code = None
        
        self.check_errors()
             
        
    def get_text_parts(self):
        parts = [t.strip() for t in self.raw_text.lower().split(" ") if t]                    
        return parts
    
    def check_errors(self):
        
        sms_parts = self.get_text_parts()#;print sms_parts
        
        if len(sms_parts) > 4:
            ## parse mother national_id
            try:
                self.mother = self.get_patient_id(" %s " % sms_parts[CHILD_DEATH_SMS_INDEXES['mother']])
            except IndexError, e:
                raise Exception(_("Patient ID is missing!"))

            ## parse child number
            try:
                self.child_number = self.get_child_number(" %s " % sms_parts[CHILD_DEATH_SMS_INDEXES['child_number']])
            except IndexError, e:
                raise Exception(_("Child Number Is missing!"))
            
            ## parse date of birth
            try:
                self.date_of_birth = self.get_date_of_birth(" %s " % sms_parts[CHILD_DEATH_SMS_INDEXES['date_of_birth']])
            except IndexError, e:
                raise Exception(_("Date of delivery Is missing!"))
            
            ## parse delivery location
            try:
                self.location = self.get_location( " %s " % sms_parts[CHILD_DEATH_SMS_INDEXES['location']])
            except IndexError, e:
                raise Exception(_("Location is missing!"))
            
            ## parse Death Code
            try:
                self.death_code = self.get_death_code( " %s " % sms_parts[CHILD_DEATH_SMS_INDEXES['death_code']])
            except IndexError, e:
                raise Exception(_("Death Code Is missing!"))
            
        else:
            ## parse mother national_id
            try:
                self.mother = self.get_patient_id(" %s " % sms_parts[WOMAN_DEATH_SMS_INDEXES['mother']])
            except IndexError, e:
                raise Exception(_("Patient ID is missing!"))
            
            ## parse delivery location
            try:
                self.location = self.get_location( " %s " % sms_parts[WOMAN_DEATH_SMS_INDEXES['location']])
            except IndexError, e:
                raise Exception(_("Location is missing!"))
            
            ## parse Death Code
            try:
                self.death_code = self.get_death_code( " %s " % sms_parts[WOMAN_DEATH_SMS_INDEXES['death_code']])
            except IndexError, e:
                raise Exception(_("Death Code Is missing!"))
                
        return True
    
    def get_patient_id(self, text):
        nid = re.search("\s(\d+)\s", text)
        if not nid:
            raise Exception(_("Patient ID Is missing."))
        elif len(nid.group(1)) != 16:
            raise Exception(_("Patient ID must be 16 digits of national ID Or 10 digits of CHW Phone Number + 6 digits of ddmmyy"))
        else:
            return nid.group(1)
        
    def get_child_number(self, text):
        chino = re.search("\s([0-9]+)\s", text)
        if not chino:
            raise Exception(_("Child Number Is missing."))
        elif len(chino.group(1)) != 2 or not chino.group(1).startswith("0") or chino.group(1).endswith("0"):
            raise Exception(_("Please check you have the correct child number. This number should be a 2 digit number, the first digit is always 0 and second digit varies between 1-8"))
        else:
            return chino.group(1)
    

        
              
    def get_date_of_birth(self, text):
        """
        Parse the date of birth from a raw SMS text.
        This date cannot be in the future.
        
        """
        today = date.today()
        dob = get_date(text)
        if dob > today:
            raise Exception(_("Date of delivery should be equal to or less then current date"))
        else:
            return dob
            
    def get_location(self, text):
        loc = re.search("\s(%s)\s" % DEATH_LOCATION_PATTERN, text)
        if loc:
            return loc.group(1)
        else:
            raise Exception(_("Location is missing! Please be sure that you have entered the appropriate Birth location. It should be HO, HP, OR or CL."))
        
    def get_death_code(self, text):
        death_code = re.search("\s(%s)\s" % DEATH_CODE_PATTERN, text)
            
        if death_code:
            death_code = death_code.group(1)
            #print death_code
            if not self.child_number and not self.date_of_birth:
                if death_code != 'md':
                    raise Exception(_("Maternal Death Code Is missing! It should be MD because there is no child number and date of birth in this SMS."))
            return death_code
        else:
            raise Exception(_("Death Code Is missing! Please be sure that you have entered the appropriate Death Code. It should be MD, CD, or ND."))


# class DthHandler (KeywordHandler):
class DthHandler (NovaHandler):
    """
    Death REGISTRATION
    """

    keyword = "dth"
    
    def filter(self):
        if not getattr(message, 'connection', None):
            self.respond(_("You need to be registered first, use the REG keyword"))
            return True 
    def help(self):
        self.respond("The correct format message is: DTH MOTHER_ID CHILD_NUMBER DATE_OF_BIRTH DEATH_CODE")

    def classic_handle(self, text):
        #print self.msg.text
        return self.death(self.msg)
        self.respond(text)

    def death(self, message):

        try: activate(message.contact.language)
        except:    activate('rw')

    	try:
            message.reporter = message_reporter(message)#Reporter.objects.filter(national_id = message.connection.contact.name )[0]
        except Exception, e:
            message.respond(_("You need to be registered first, Please contact your supervisor!"))
            return True

        """m = re.search("dth\s+(\d+)\s([0-9]+)\s([0-9.]+)\s(hp|cl|or|ho)\s(nd|cd|md)\s?(.*)", message.text, re.IGNORECASE)
        
        if not m:           
            m = re.search("dth\s+(\d+)\s(hp|cl|or|ho)\s(nd|cd|md)\s?(.*)", message.text, re.IGNORECASE) 
            if not m:
                message.respond(_("The correct format message is: DTH MOTHER_ID CHILD_NUMBER DATE_OF_BIRTH DEATH_CODE"))
                return True

        try:    nid = read_nid(message, m.group(1))
        except Exception, e:
            # there were invalid fields, respond and exit
            message.respond("%s" % e)
            return True
        
        if len(m.groups()) > 5:
            number = m.group(2)
            chidob = m.group(3)
            location = m.group(4)
            death = m.group(5)
        else:
            number = None
            chidob = None
            location = m.group(2)
            death = m.group(3)    

        ibibazo = "%s %s" % ( location, death)

        """            
        try:
        
            msg = DeathRecord(message.text)
            nid = msg.mother
            chino = msg.child_number
            chidob = msg.date_of_birth
            location = msg.location
            death = msg.death_code
            ibibazo = "%s %s" % ( location, death)

        except Exception, e:
            # there were invalid fields, respond and exit
            message.respond("%s" % e)
            return True
            
        # get or create the patient
        patient = get_or_create_patient(message.reporter, nid)

        report = create_report('Death', patient, message.reporter)
        
        # Line below may be needed in case Risk reports are sent without previous Pregnancy reports
        #location = message.reporter.location
        
        # read our fields
        
        try:
            (fields, dob) = read_fields(ibibazo, False, False)
    	    ##if chidob:  dob = parse_dob(chidob)
            dob = chidob
        except Exception, e:
            # there were invalid fields, respond and exit
            message.respond("%s" % e)
            return True
        
        # set the dob for the child if we got one
        if dob:
            report.date = dob

        # save the report
        for f in fields:
            if f.type in FieldType.objects.filter(category__name = 'Red Alert Codes'):
                message.respond(_("%(key)s:%(red)s is a red alert, please see how to report a red alert and try again.")\
                                         % { 'key': f.type.key,'red' : f.type.kw})
                return True
        if not report.has_dups():
        	report.save()
        else:
    		message.respond(_("This report has been recorded, and we cannot duplicate it again. Thank you!"))
    		return True
        

	    # then associate all our fields with it
        
        if chino:  fields.append(read_number(chino))
        
        for field in fields:
            if field:
                
                try:
                    if field.type.key == 'cd' and (report.created.date() - report.date).days < 42: field.type = FieldType.objects.get(key = 'nd')
                except:
                    pass
                
                field.report = report
                field.save()
                report.fields.add(field)

	    # either send back the advice text or our default msg
        try:	response = run_triggers(message, report)
        except:	response = None
        if response:
            message.respond(response)
        else:
            message.respond(_("Thank you! Death report submitted successfully."))
            
        # cc the supervisor if there is one
        try:	cc_supervisor(message, report)
        except:	pass      
            	
        return True 

