PGDMP     #    8                r            thousanddays    9.1.13    9.1.13 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           1262    16388    thousanddays    DATABASE     ~   CREATE DATABASE thousanddays WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_GB.UTF-8';
    DROP DATABASE thousanddays;
             thousanddays    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    5            �           0    0    public    ACL     �   REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;
                  postgres    false    5            �            3079    11677    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            �           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    216            �            1259    16428 
   auth_group    TABLE     ^   CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);
    DROP TABLE public.auth_group;
       public         thousanddays    false    5            �            1259    16426    auth_group_id_seq    SEQUENCE     s   CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       thousanddays    false    168    5            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;
            public       thousanddays    false    167            �            1259    16413    auth_group_permissions    TABLE     �   CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         thousanddays    false    5            �            1259    16411    auth_group_permissions_id_seq    SEQUENCE        CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       thousanddays    false    5    166            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;
            public       thousanddays    false    165            �            1259    16403    auth_permission    TABLE     �   CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         thousanddays    false    5            �            1259    16401    auth_permission_id_seq    SEQUENCE     x   CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       thousanddays    false    5    164            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;
            public       thousanddays    false    163            �            1259    16473 	   auth_user    TABLE     �  CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         thousanddays    false    5            �            1259    16443    auth_user_groups    TABLE     x   CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         thousanddays    false    5            �            1259    16441    auth_user_groups_id_seq    SEQUENCE     y   CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       thousanddays    false    170    5            �           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;
            public       thousanddays    false    169            �            1259    16471    auth_user_id_seq    SEQUENCE     r   CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       thousanddays    false    5    174            �           0    0    auth_user_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;
            public       thousanddays    false    173            �            1259    16458    auth_user_user_permissions    TABLE     �   CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         thousanddays    false    5            �            1259    16456 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       thousanddays    false    5    172            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;
            public       thousanddays    false    171            �            1259    16639 
   ccmreports    TABLE     �  CREATE TABLE ccmreports (
    indexcol integer NOT NULL,
    idfield text,
    numberfield text,
    datefield text,
    ccmsymptomcodefield_di text,
    ccmsymptomcodefield_ma text,
    ccmsymptomcodefield_pc text,
    ccmsymptomcodefield_oi text,
    ccmsymptomcodefield_np text,
    ccmsymptomcodefield_ib text,
    ccmsymptomcodefield_db text,
    ccmsymptomcodefield_nv text,
    ccminterventionfield text,
    muacfield text
);
    DROP TABLE public.ccmreports;
       public         thousanddays    false    5            �            1259    16637    ccmreports_indexcol_seq    SEQUENCE     y   CREATE SEQUENCE ccmreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.ccmreports_indexcol_seq;
       public       thousanddays    false    199    5            �           0    0    ccmreports_indexcol_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE ccmreports_indexcol_seq OWNED BY ccmreports.indexcol;
            public       thousanddays    false    198            �            1259    16666    childreports    TABLE     ^  CREATE TABLE childreports (
    indexcol integer NOT NULL,
    idfield text,
    numberfield text,
    datefield text,
    vaccinationfield text,
    vaccinationcompletionfield text,
    chisymptomcodefield_np text,
    chisymptomcodefield_ib text,
    chisymptomcodefield_db text,
    locationfield text,
    weightfield text,
    muacfield text
);
     DROP TABLE public.childreports;
       public         thousanddays    false    5            �            1259    16664    childreports_indexcol_seq    SEQUENCE     {   CREATE SEQUENCE childreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.childreports_indexcol_seq;
       public       thousanddays    false    205    5            �           0    0    childreports_indexcol_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE childreports_indexcol_seq OWNED BY childreports.indexcol;
            public       thousanddays    false    204            �            1259    16711 
   cmrreports    TABLE     �  CREATE TABLE cmrreports (
    indexcol integer NOT NULL,
    idfield text,
    numberfield text,
    datefield text,
    cmrsymptomcodefield_di text,
    cmrsymptomcodefield_ma text,
    cmrsymptomcodefield_pc text,
    cmrsymptomcodefield_oi text,
    cmrsymptomcodefield_np text,
    cmrsymptomcodefield_ib text,
    cmrsymptomcodefield_db text,
    cmrsymptomcodefield_nv text,
    cmrinterventionfield text,
    childstatusfield text
);
    DROP TABLE public.cmrreports;
       public         thousanddays    false    5            �            1259    16709    cmrreports_indexcol_seq    SEQUENCE     y   CREATE SEQUENCE cmrreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.cmrreports_indexcol_seq;
       public       thousanddays    false    5    215            �           0    0    cmrreports_indexcol_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE cmrreports_indexcol_seq OWNED BY cmrreports.indexcol;
            public       thousanddays    false    214            �            1259    16621    deathreports    TABLE     �   CREATE TABLE deathreports (
    indexcol integer NOT NULL,
    idfield text,
    numberfield text,
    datefield text,
    locationfield text,
    deathfield text
);
     DROP TABLE public.deathreports;
       public         thousanddays    false    5            �            1259    16619    deathreports_indexcol_seq    SEQUENCE     {   CREATE SEQUENCE deathreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.deathreports_indexcol_seq;
       public       thousanddays    false    5    195            �           0    0    deathreports_indexcol_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE deathreports_indexcol_seq OWNED BY deathreports.indexcol;
            public       thousanddays    false    194            �            1259    16391    django_admin_log    TABLE     �  CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         thousanddays    false    1963    5            �            1259    16389    django_admin_log_id_seq    SEQUENCE     y   CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       thousanddays    false    5    162            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;
            public       thousanddays    false    161            �            1259    16498    django_content_type    TABLE     �   CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         thousanddays    false    5            �            1259    16496    django_content_type_id_seq    SEQUENCE     |   CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       thousanddays    false    5    176            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;
            public       thousanddays    false    175            �            1259    16516    django_session    TABLE     �   CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         thousanddays    false    5            �            1259    16675 
   nbcreports    TABLE       CREATE TABLE nbcreports (
    indexcol integer NOT NULL,
    idfield text,
    numberfield text,
    nbcfield text,
    datefield text,
    nbcsymptomcodefield_sb text,
    nbcsymptomcodefield_rb text,
    nbcsymptomcodefield_np text,
    nbcsymptomcodefield_af text,
    nbcsymptomcodefield_ci text,
    nbcsymptomcodefield_cm text,
    nbcsymptomcodefield_ib text,
    nbcsymptomcodefield_db text,
    nbcsymptomcodefield_pm text,
    nbcbreastfeedfield text,
    nbcinterventionfield text,
    newbornhealthstatusfield text
);
    DROP TABLE public.nbcreports;
       public         thousanddays    false    5            �            1259    16673    nbcreports_indexcol_seq    SEQUENCE     y   CREATE SEQUENCE nbcreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.nbcreports_indexcol_seq;
       public       thousanddays    false    207    5            �           0    0    nbcreports_indexcol_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE nbcreports_indexcol_seq OWNED BY nbcreports.indexcol;
            public       thousanddays    false    206            �            1259    16693 
   pncreports    TABLE     +  CREATE TABLE pncreports (
    indexcol integer NOT NULL,
    idfield text,
    pncfield text,
    datefield text,
    symptomcodefield_af text,
    symptomcodefield_ch text,
    symptomcodefield_ci text,
    symptomcodefield_cm text,
    symptomcodefield_ib text,
    symptomcodefield_db text,
    symptomcodefield_di text,
    symptomcodefield_ds text,
    symptomcodefield_fe text,
    symptomcodefield_fp text,
    symptomcodefield_hy text,
    symptomcodefield_ja text,
    symptomcodefield_ma text,
    symptomcodefield_np text,
    symptomcodefield_ns text,
    symptomcodefield_oe text,
    symptomcodefield_pc text,
    symptomcodefield_rb text,
    symptomcodefield_sa text,
    symptomcodefield_sb text,
    symptomcodefield_vo text,
    pncinterventionfield text,
    motherhealthstatusfield text
);
    DROP TABLE public.pncreports;
       public         thousanddays    false    5            �            1259    16691    pncreports_indexcol_seq    SEQUENCE     y   CREATE SEQUENCE pncreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.pncreports_indexcol_seq;
       public       thousanddays    false    5    211            �           0    0    pncreports_indexcol_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE pncreports_indexcol_seq OWNED BY pncreports.indexcol;
            public       thousanddays    false    210            �            1259    16630    pregreports    TABLE     B  CREATE TABLE pregreports (
    indexcol integer NOT NULL,
    idfield text,
    datefield text,
    lmpdatefield text,
    gravidityfield text,
    parityfield text,
    prevpregcodefield_gs text,
    prevpregcodefield_mu text,
    prevpregcodefield_hd text,
    prevpregcodefield_rm text,
    prevpregcodefield_ol text,
    prevpregcodefield_yg text,
    prevpregcodefield_nr text,
    prevpregcodefield_to text,
    prevpregcodefield_hw text,
    prevpregcodefield_nt text,
    prevpregcodefield_nh text,
    prevpregcodefield_kx text,
    prevpregcodefield_yj text,
    prevpregcodefield_lz text,
    symptomcodefield_af text,
    symptomcodefield_ch text,
    symptomcodefield_ci text,
    symptomcodefield_cm text,
    symptomcodefield_ib text,
    symptomcodefield_db text,
    symptomcodefield_di text,
    symptomcodefield_ds text,
    symptomcodefield_fe text,
    symptomcodefield_fp text,
    symptomcodefield_hy text,
    symptomcodefield_ja text,
    symptomcodefield_ma text,
    symptomcodefield_np text,
    symptomcodefield_ns text,
    symptomcodefield_oe text,
    symptomcodefield_pc text,
    symptomcodefield_rb text,
    symptomcodefield_sa text,
    symptomcodefield_sb text,
    symptomcodefield_vo text,
    locationfield text,
    weightfield text,
    heightfield text,
    toiletfield text,
    handwashfield text
);
    DROP TABLE public.pregreports;
       public         thousanddays    false    5            �            1259    16628    pregreports_indexcol_seq    SEQUENCE     z   CREATE SEQUENCE pregreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.pregreports_indexcol_seq;
       public       thousanddays    false    5    197            �           0    0    pregreports_indexcol_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE pregreports_indexcol_seq OWNED BY pregreports.indexcol;
            public       thousanddays    false    196            �            1259    16587 
   redreports    TABLE     �  CREATE TABLE redreports (
    indexcol integer NOT NULL,
    redsymptomcodefield_ap text,
    redsymptomcodefield_co text,
    redsymptomcodefield_he text,
    redsymptomcodefield_la text,
    redsymptomcodefield_mc text,
    redsymptomcodefield_pa text,
    redsymptomcodefield_ps text,
    redsymptomcodefield_sc text,
    redsymptomcodefield_sl text,
    redsymptomcodefield_un text,
    locationfield text
);
    DROP TABLE public.redreports;
       public         thousanddays    false    5            �            1259    16585    redreports_indexcol_seq    SEQUENCE     y   CREATE SEQUENCE redreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.redreports_indexcol_seq;
       public       thousanddays    false    5    187            �           0    0    redreports_indexcol_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE redreports_indexcol_seq OWNED BY redreports.indexcol;
            public       thousanddays    false    186            �            1259    16657    redresultreports    TABLE     
  CREATE TABLE redresultreports (
    indexcol integer NOT NULL,
    idfield text,
    datefield text,
    redsymptomcodefield_ap text,
    redsymptomcodefield_co text,
    redsymptomcodefield_he text,
    redsymptomcodefield_la text,
    redsymptomcodefield_mc text,
    redsymptomcodefield_pa text,
    redsymptomcodefield_ps text,
    redsymptomcodefield_sc text,
    redsymptomcodefield_sl text,
    redsymptomcodefield_un text,
    locationfield text,
    redinterventionfield text,
    motherhealthstatusfield text
);
 $   DROP TABLE public.redresultreports;
       public         thousanddays    false    5            �            1259    16655    redresultreports_indexcol_seq    SEQUENCE        CREATE SEQUENCE redresultreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.redresultreports_indexcol_seq;
       public       thousanddays    false    203    5            �           0    0    redresultreports_indexcol_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE redresultreports_indexcol_seq OWNED BY redresultreports.indexcol;
            public       thousanddays    false    202            �            1259    16702 
   refreports    TABLE     W   CREATE TABLE refreports (
    indexcol integer NOT NULL,
    phonebasedidfield text
);
    DROP TABLE public.refreports;
       public         thousanddays    false    5            �            1259    16700    refreports_indexcol_seq    SEQUENCE     y   CREATE SEQUENCE refreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.refreports_indexcol_seq;
       public       thousanddays    false    5    213            �           0    0    refreports_indexcol_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE refreports_indexcol_seq OWNED BY refreports.indexcol;
            public       thousanddays    false    212            �            1259    16684    resultreports    TABLE     �  CREATE TABLE resultreports (
    indexcol integer NOT NULL,
    idfield text,
    risksymptomcodefield_vo text,
    risksymptomcodefield_pc text,
    risksymptomcodefield_oe text,
    risksymptomcodefield_ns text,
    risksymptomcodefield_ma text,
    risksymptomcodefield_ja text,
    risksymptomcodefield_fp text,
    risksymptomcodefield_fe text,
    risksymptomcodefield_ds text,
    risksymptomcodefield_di text,
    risksymptomcodefield_sa text,
    risksymptomcodefield_rb text,
    risksymptomcodefield_hy text,
    risksymptomcodefield_ch text,
    risksymptomcodefield_af text,
    locationfield text,
    riskinterventionfield text,
    motherhealthstatusfield text
);
 !   DROP TABLE public.resultreports;
       public         thousanddays    false    5            �            1259    16682    resultreports_indexcol_seq    SEQUENCE     |   CREATE SEQUENCE resultreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.resultreports_indexcol_seq;
       public       thousanddays    false    209    5            �           0    0    resultreports_indexcol_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE resultreports_indexcol_seq OWNED BY resultreports.indexcol;
            public       thousanddays    false    208            �            1259    16596    revencereports    TABLE     �   CREATE TABLE revencereports (
    indexcol integer NOT NULL,
    textfield_revence text,
    textfield_kato text,
    textfield_kalibwani text,
    revfield_revence text,
    revfield_kato text,
    revfield_kalibwani text
);
 "   DROP TABLE public.revencereports;
       public         thousanddays    false    5            �            1259    16594    revencereports_indexcol_seq    SEQUENCE     }   CREATE SEQUENCE revencereports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.revencereports_indexcol_seq;
       public       thousanddays    false    5    189            �           0    0    revencereports_indexcol_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE revencereports_indexcol_seq OWNED BY revencereports.indexcol;
            public       thousanddays    false    188            �            1259    16612    riskreports    TABLE     z  CREATE TABLE riskreports (
    indexcol integer NOT NULL,
    idfield text,
    risksymptomcodefield_vo text,
    risksymptomcodefield_pc text,
    risksymptomcodefield_oe text,
    risksymptomcodefield_ns text,
    risksymptomcodefield_ma text,
    risksymptomcodefield_ja text,
    risksymptomcodefield_fp text,
    risksymptomcodefield_fe text,
    risksymptomcodefield_ds text,
    risksymptomcodefield_di text,
    risksymptomcodefield_sa text,
    risksymptomcodefield_rb text,
    risksymptomcodefield_hy text,
    risksymptomcodefield_ch text,
    risksymptomcodefield_af text,
    locationfield text,
    weightfield text
);
    DROP TABLE public.riskreports;
       public         thousanddays    false    5            �            1259    16610    riskreports_indexcol_seq    SEQUENCE     z   CREATE SEQUENCE riskreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.riskreports_indexcol_seq;
       public       thousanddays    false    5    193            �           0    0    riskreports_indexcol_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE riskreports_indexcol_seq OWNED BY riskreports.indexcol;
            public       thousanddays    false    192            �            1259    16548    thoureport_smserror    TABLE     >   CREATE TABLE thoureport_smserror (
    id integer NOT NULL
);
 '   DROP TABLE public.thoureport_smserror;
       public         thousanddays    false    5            �            1259    16546    thoureport_smserror_id_seq    SEQUENCE     |   CREATE SEQUENCE thoureport_smserror_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.thoureport_smserror_id_seq;
       public       thousanddays    false    183    5            �           0    0    thoureport_smserror_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE thoureport_smserror_id_seq OWNED BY thoureport_smserror.id;
            public       thousanddays    false    182            �            1259    16526    thoureport_storederrormessage    TABLE     `   CREATE TABLE thoureport_storederrormessage (
    id integer NOT NULL,
    text text NOT NULL
);
 1   DROP TABLE public.thoureport_storederrormessage;
       public         thousanddays    false    5            �            1259    16524 $   thoureport_storederrormessage_id_seq    SEQUENCE     �   CREATE SEQUENCE thoureport_storederrormessage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.thoureport_storederrormessage_id_seq;
       public       thousanddays    false    179    5            �           0    0 $   thoureport_storederrormessage_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE thoureport_storederrormessage_id_seq OWNED BY thoureport_storederrormessage.id;
            public       thousanddays    false    178            �            1259    16576    thoureport_storedresponse    TABLE     t   CREATE TABLE thoureport_storedresponse (
    id integer NOT NULL,
    text text NOT NULL,
    code text NOT NULL
);
 -   DROP TABLE public.thoureport_storedresponse;
       public         thousanddays    false    5            �            1259    16574     thoureport_storedresponse_id_seq    SEQUENCE     �   CREATE SEQUENCE thoureport_storedresponse_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.thoureport_storedresponse_id_seq;
       public       thousanddays    false    5    185            �           0    0     thoureport_storedresponse_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE thoureport_storedresponse_id_seq OWNED BY thoureport_storedresponse.id;
            public       thousanddays    false    184            �            1259    16537    thoureport_storedsms    TABLE     �   CREATE TABLE thoureport_storedsms (
    id integer NOT NULL,
    message text NOT NULL,
    sender text NOT NULL,
    "when" timestamp with time zone NOT NULL
);
 (   DROP TABLE public.thoureport_storedsms;
       public         thousanddays    false    5            �            1259    16535    thoureport_storedsms_id_seq    SEQUENCE     }   CREATE SEQUENCE thoureport_storedsms_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.thoureport_storedsms_id_seq;
       public       thousanddays    false    5    181            �           0    0    thoureport_storedsms_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE thoureport_storedsms_id_seq OWNED BY thoureport_storedsms.id;
            public       thousanddays    false    180            �            1259    16605    thousanddays_reports    TABLE     �   CREATE TABLE thousanddays_reports (
    indexcol integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL
);
 (   DROP TABLE public.thousanddays_reports;
       public         thousanddays    false    1978    5            �            1259    16603 !   thousanddays_reports_indexcol_seq    SEQUENCE     �   CREATE SEQUENCE thousanddays_reports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.thousanddays_reports_indexcol_seq;
       public       thousanddays    false    191    5            �           0    0 !   thousanddays_reports_indexcol_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE thousanddays_reports_indexcol_seq OWNED BY thousanddays_reports.indexcol;
            public       thousanddays    false    190            �            1259    16648    timothyreports    TABLE     �   CREATE TABLE timothyreports (
    indexcol integer NOT NULL,
    timfield_timothy text,
    timfield_kaboya text,
    timfield_kalimba text
);
 "   DROP TABLE public.timothyreports;
       public         thousanddays    false    5            �            1259    16646    timothyreports_indexcol_seq    SEQUENCE     }   CREATE SEQUENCE timothyreports_indexcol_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.timothyreports_indexcol_seq;
       public       thousanddays    false    5    201            �           0    0    timothyreports_indexcol_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE timothyreports_indexcol_seq OWNED BY timothyreports.indexcol;
            public       thousanddays    false    200            �           2604    16431    id    DEFAULT     `   ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    167    168    168            �           2604    16416    id    DEFAULT     x   ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    165    166    166            �           2604    16406    id    DEFAULT     j   ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    163    164    164            �           2604    16476    id    DEFAULT     ^   ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    174    173    174            �           2604    16446    id    DEFAULT     l   ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    169    170    170            �           2604    16461    id    DEFAULT     �   ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    172    171    172            �           2604    16642    indexcol    DEFAULT     l   ALTER TABLE ONLY ccmreports ALTER COLUMN indexcol SET DEFAULT nextval('ccmreports_indexcol_seq'::regclass);
 B   ALTER TABLE public.ccmreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    198    199    199            �           2604    16669    indexcol    DEFAULT     p   ALTER TABLE ONLY childreports ALTER COLUMN indexcol SET DEFAULT nextval('childreports_indexcol_seq'::regclass);
 D   ALTER TABLE public.childreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    204    205    205            �           2604    16714    indexcol    DEFAULT     l   ALTER TABLE ONLY cmrreports ALTER COLUMN indexcol SET DEFAULT nextval('cmrreports_indexcol_seq'::regclass);
 B   ALTER TABLE public.cmrreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    214    215    215            �           2604    16624    indexcol    DEFAULT     p   ALTER TABLE ONLY deathreports ALTER COLUMN indexcol SET DEFAULT nextval('deathreports_indexcol_seq'::regclass);
 D   ALTER TABLE public.deathreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    195    194    195            �           2604    16394    id    DEFAULT     l   ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    162    161    162            �           2604    16501    id    DEFAULT     r   ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    176    175    176            �           2604    16678    indexcol    DEFAULT     l   ALTER TABLE ONLY nbcreports ALTER COLUMN indexcol SET DEFAULT nextval('nbcreports_indexcol_seq'::regclass);
 B   ALTER TABLE public.nbcreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    207    206    207            �           2604    16696    indexcol    DEFAULT     l   ALTER TABLE ONLY pncreports ALTER COLUMN indexcol SET DEFAULT nextval('pncreports_indexcol_seq'::regclass);
 B   ALTER TABLE public.pncreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    211    210    211            �           2604    16633    indexcol    DEFAULT     n   ALTER TABLE ONLY pregreports ALTER COLUMN indexcol SET DEFAULT nextval('pregreports_indexcol_seq'::regclass);
 C   ALTER TABLE public.pregreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    196    197    197            �           2604    16590    indexcol    DEFAULT     l   ALTER TABLE ONLY redreports ALTER COLUMN indexcol SET DEFAULT nextval('redreports_indexcol_seq'::regclass);
 B   ALTER TABLE public.redreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    186    187    187            �           2604    16660    indexcol    DEFAULT     x   ALTER TABLE ONLY redresultreports ALTER COLUMN indexcol SET DEFAULT nextval('redresultreports_indexcol_seq'::regclass);
 H   ALTER TABLE public.redresultreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    202    203    203            �           2604    16705    indexcol    DEFAULT     l   ALTER TABLE ONLY refreports ALTER COLUMN indexcol SET DEFAULT nextval('refreports_indexcol_seq'::regclass);
 B   ALTER TABLE public.refreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    213    212    213            �           2604    16687    indexcol    DEFAULT     r   ALTER TABLE ONLY resultreports ALTER COLUMN indexcol SET DEFAULT nextval('resultreports_indexcol_seq'::regclass);
 E   ALTER TABLE public.resultreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    208    209    209            �           2604    16599    indexcol    DEFAULT     t   ALTER TABLE ONLY revencereports ALTER COLUMN indexcol SET DEFAULT nextval('revencereports_indexcol_seq'::regclass);
 F   ALTER TABLE public.revencereports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    188    189    189            �           2604    16615    indexcol    DEFAULT     n   ALTER TABLE ONLY riskreports ALTER COLUMN indexcol SET DEFAULT nextval('riskreports_indexcol_seq'::regclass);
 C   ALTER TABLE public.riskreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    193    192    193            �           2604    16551    id    DEFAULT     r   ALTER TABLE ONLY thoureport_smserror ALTER COLUMN id SET DEFAULT nextval('thoureport_smserror_id_seq'::regclass);
 E   ALTER TABLE public.thoureport_smserror ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    183    182    183            �           2604    16529    id    DEFAULT     �   ALTER TABLE ONLY thoureport_storederrormessage ALTER COLUMN id SET DEFAULT nextval('thoureport_storederrormessage_id_seq'::regclass);
 O   ALTER TABLE public.thoureport_storederrormessage ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    178    179    179            �           2604    16579    id    DEFAULT     ~   ALTER TABLE ONLY thoureport_storedresponse ALTER COLUMN id SET DEFAULT nextval('thoureport_storedresponse_id_seq'::regclass);
 K   ALTER TABLE public.thoureport_storedresponse ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    184    185    185            �           2604    16540    id    DEFAULT     t   ALTER TABLE ONLY thoureport_storedsms ALTER COLUMN id SET DEFAULT nextval('thoureport_storedsms_id_seq'::regclass);
 F   ALTER TABLE public.thoureport_storedsms ALTER COLUMN id DROP DEFAULT;
       public       thousanddays    false    180    181    181            �           2604    16608    indexcol    DEFAULT     �   ALTER TABLE ONLY thousanddays_reports ALTER COLUMN indexcol SET DEFAULT nextval('thousanddays_reports_indexcol_seq'::regclass);
 L   ALTER TABLE public.thousanddays_reports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    191    190    191            �           2604    16651    indexcol    DEFAULT     t   ALTER TABLE ONLY timothyreports ALTER COLUMN indexcol SET DEFAULT nextval('timothyreports_indexcol_seq'::regclass);
 F   ALTER TABLE public.timothyreports ALTER COLUMN indexcol DROP DEFAULT;
       public       thousanddays    false    200    201    201            q          0    16428 
   auth_group 
   TABLE DATA               '   COPY auth_group (id, name) FROM stdin;
    public       thousanddays    false    168    2209         �           0    0    auth_group_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('auth_group_id_seq', 1, false);
            public       thousanddays    false    167            o          0    16413    auth_group_permissions 
   TABLE DATA               F   COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       thousanddays    false    166    2209   %      �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);
            public       thousanddays    false    165            m          0    16403    auth_permission 
   TABLE DATA               G   COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       thousanddays    false    164    2209   B      �           0    0    auth_permission_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('auth_permission_id_seq', 30, true);
            public       thousanddays    false    163            w          0    16473 	   auth_user 
   TABLE DATA               �   COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public       thousanddays    false    174    2209   �      s          0    16443    auth_user_groups 
   TABLE DATA               :   COPY auth_user_groups (id, user_id, group_id) FROM stdin;
    public       thousanddays    false    170    2209   2      �           0    0    auth_user_groups_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);
            public       thousanddays    false    169            �           0    0    auth_user_id_seq    SEQUENCE SET     7   SELECT pg_catalog.setval('auth_user_id_seq', 1, true);
            public       thousanddays    false    173            u          0    16458    auth_user_user_permissions 
   TABLE DATA               I   COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       thousanddays    false    172    2209   O      �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);
            public       thousanddays    false    171            �          0    16639 
   ccmreports 
   TABLE DATA               )  COPY ccmreports (indexcol, idfield, numberfield, datefield, ccmsymptomcodefield_di, ccmsymptomcodefield_ma, ccmsymptomcodefield_pc, ccmsymptomcodefield_oi, ccmsymptomcodefield_np, ccmsymptomcodefield_ib, ccmsymptomcodefield_db, ccmsymptomcodefield_nv, ccminterventionfield, muacfield) FROM stdin;
    public       thousanddays    false    199    2209   l      �           0    0    ccmreports_indexcol_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('ccmreports_indexcol_seq', 1, false);
            public       thousanddays    false    198            �          0    16666    childreports 
   TABLE DATA               �   COPY childreports (indexcol, idfield, numberfield, datefield, vaccinationfield, vaccinationcompletionfield, chisymptomcodefield_np, chisymptomcodefield_ib, chisymptomcodefield_db, locationfield, weightfield, muacfield) FROM stdin;
    public       thousanddays    false    205    2209   �      �           0    0    childreports_indexcol_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('childreports_indexcol_seq', 1, false);
            public       thousanddays    false    204            �          0    16711 
   cmrreports 
   TABLE DATA               0  COPY cmrreports (indexcol, idfield, numberfield, datefield, cmrsymptomcodefield_di, cmrsymptomcodefield_ma, cmrsymptomcodefield_pc, cmrsymptomcodefield_oi, cmrsymptomcodefield_np, cmrsymptomcodefield_ib, cmrsymptomcodefield_db, cmrsymptomcodefield_nv, cmrinterventionfield, childstatusfield) FROM stdin;
    public       thousanddays    false    215    2209   �      �           0    0    cmrreports_indexcol_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('cmrreports_indexcol_seq', 1, false);
            public       thousanddays    false    214            �          0    16621    deathreports 
   TABLE DATA               e   COPY deathreports (indexcol, idfield, numberfield, datefield, locationfield, deathfield) FROM stdin;
    public       thousanddays    false    195    2209   �      �           0    0    deathreports_indexcol_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('deathreports_indexcol_seq', 1, false);
            public       thousanddays    false    194            k          0    16391    django_admin_log 
   TABLE DATA               �   COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
    public       thousanddays    false    162    2209   �      �           0    0    django_admin_log_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);
            public       thousanddays    false    161            y          0    16498    django_content_type 
   TABLE DATA               B   COPY django_content_type (id, name, app_label, model) FROM stdin;
    public       thousanddays    false    176    2209   �      �           0    0    django_content_type_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('django_content_type_id_seq', 10, true);
            public       thousanddays    false    175            z          0    16516    django_session 
   TABLE DATA               I   COPY django_session (session_key, session_data, expire_date) FROM stdin;
    public       thousanddays    false    177    2209   �      �          0    16675 
   nbcreports 
   TABLE DATA               n  COPY nbcreports (indexcol, idfield, numberfield, nbcfield, datefield, nbcsymptomcodefield_sb, nbcsymptomcodefield_rb, nbcsymptomcodefield_np, nbcsymptomcodefield_af, nbcsymptomcodefield_ci, nbcsymptomcodefield_cm, nbcsymptomcodefield_ib, nbcsymptomcodefield_db, nbcsymptomcodefield_pm, nbcbreastfeedfield, nbcinterventionfield, newbornhealthstatusfield) FROM stdin;
    public       thousanddays    false    207    2209   �      �           0    0    nbcreports_indexcol_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('nbcreports_indexcol_seq', 1, false);
            public       thousanddays    false    206            �          0    16693 
   pncreports 
   TABLE DATA               -  COPY pncreports (indexcol, idfield, pncfield, datefield, symptomcodefield_af, symptomcodefield_ch, symptomcodefield_ci, symptomcodefield_cm, symptomcodefield_ib, symptomcodefield_db, symptomcodefield_di, symptomcodefield_ds, symptomcodefield_fe, symptomcodefield_fp, symptomcodefield_hy, symptomcodefield_ja, symptomcodefield_ma, symptomcodefield_np, symptomcodefield_ns, symptomcodefield_oe, symptomcodefield_pc, symptomcodefield_rb, symptomcodefield_sa, symptomcodefield_sb, symptomcodefield_vo, pncinterventionfield, motherhealthstatusfield) FROM stdin;
    public       thousanddays    false    211    2209          �           0    0    pncreports_indexcol_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('pncreports_indexcol_seq', 1, false);
            public       thousanddays    false    210            �          0    16630    pregreports 
   TABLE DATA               �  COPY pregreports (indexcol, idfield, datefield, lmpdatefield, gravidityfield, parityfield, prevpregcodefield_gs, prevpregcodefield_mu, prevpregcodefield_hd, prevpregcodefield_rm, prevpregcodefield_ol, prevpregcodefield_yg, prevpregcodefield_nr, prevpregcodefield_to, prevpregcodefield_hw, prevpregcodefield_nt, prevpregcodefield_nh, prevpregcodefield_kx, prevpregcodefield_yj, prevpregcodefield_lz, symptomcodefield_af, symptomcodefield_ch, symptomcodefield_ci, symptomcodefield_cm, symptomcodefield_ib, symptomcodefield_db, symptomcodefield_di, symptomcodefield_ds, symptomcodefield_fe, symptomcodefield_fp, symptomcodefield_hy, symptomcodefield_ja, symptomcodefield_ma, symptomcodefield_np, symptomcodefield_ns, symptomcodefield_oe, symptomcodefield_pc, symptomcodefield_rb, symptomcodefield_sa, symptomcodefield_sb, symptomcodefield_vo, locationfield, weightfield, heightfield, toiletfield, handwashfield) FROM stdin;
    public       thousanddays    false    197    2209         �           0    0    pregreports_indexcol_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('pregreports_indexcol_seq', 1, false);
            public       thousanddays    false    196            �          0    16587 
   redreports 
   TABLE DATA               &  COPY redreports (indexcol, redsymptomcodefield_ap, redsymptomcodefield_co, redsymptomcodefield_he, redsymptomcodefield_la, redsymptomcodefield_mc, redsymptomcodefield_pa, redsymptomcodefield_ps, redsymptomcodefield_sc, redsymptomcodefield_sl, redsymptomcodefield_un, locationfield) FROM stdin;
    public       thousanddays    false    187    2209   :      �           0    0    redreports_indexcol_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('redreports_indexcol_seq', 1, false);
            public       thousanddays    false    186            �          0    16657    redresultreports 
   TABLE DATA               o  COPY redresultreports (indexcol, idfield, datefield, redsymptomcodefield_ap, redsymptomcodefield_co, redsymptomcodefield_he, redsymptomcodefield_la, redsymptomcodefield_mc, redsymptomcodefield_pa, redsymptomcodefield_ps, redsymptomcodefield_sc, redsymptomcodefield_sl, redsymptomcodefield_un, locationfield, redinterventionfield, motherhealthstatusfield) FROM stdin;
    public       thousanddays    false    203    2209   W      �           0    0    redresultreports_indexcol_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('redresultreports_indexcol_seq', 1, false);
            public       thousanddays    false    202            �          0    16702 
   refreports 
   TABLE DATA               :   COPY refreports (indexcol, phonebasedidfield) FROM stdin;
    public       thousanddays    false    213    2209   t      �           0    0    refreports_indexcol_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('refreports_indexcol_seq', 1, false);
            public       thousanddays    false    212            �          0    16684    resultreports 
   TABLE DATA               �  COPY resultreports (indexcol, idfield, risksymptomcodefield_vo, risksymptomcodefield_pc, risksymptomcodefield_oe, risksymptomcodefield_ns, risksymptomcodefield_ma, risksymptomcodefield_ja, risksymptomcodefield_fp, risksymptomcodefield_fe, risksymptomcodefield_ds, risksymptomcodefield_di, risksymptomcodefield_sa, risksymptomcodefield_rb, risksymptomcodefield_hy, risksymptomcodefield_ch, risksymptomcodefield_af, locationfield, riskinterventionfield, motherhealthstatusfield) FROM stdin;
    public       thousanddays    false    209    2209   �      �           0    0    resultreports_indexcol_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('resultreports_indexcol_seq', 1, false);
            public       thousanddays    false    208            �          0    16596    revencereports 
   TABLE DATA               �   COPY revencereports (indexcol, textfield_revence, textfield_kato, textfield_kalibwani, revfield_revence, revfield_kato, revfield_kalibwani) FROM stdin;
    public       thousanddays    false    189    2209   �      �           0    0    revencereports_indexcol_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('revencereports_indexcol_seq', 3, true);
            public       thousanddays    false    188            �          0    16612    riskreports 
   TABLE DATA               �  COPY riskreports (indexcol, idfield, risksymptomcodefield_vo, risksymptomcodefield_pc, risksymptomcodefield_oe, risksymptomcodefield_ns, risksymptomcodefield_ma, risksymptomcodefield_ja, risksymptomcodefield_fp, risksymptomcodefield_fe, risksymptomcodefield_ds, risksymptomcodefield_di, risksymptomcodefield_sa, risksymptomcodefield_rb, risksymptomcodefield_hy, risksymptomcodefield_ch, risksymptomcodefield_af, locationfield, weightfield) FROM stdin;
    public       thousanddays    false    193    2209   �      �           0    0    riskreports_indexcol_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('riskreports_indexcol_seq', 1, false);
            public       thousanddays    false    192            �          0    16548    thoureport_smserror 
   TABLE DATA               *   COPY thoureport_smserror (id) FROM stdin;
    public       thousanddays    false    183    2209   	      �           0    0    thoureport_smserror_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('thoureport_smserror_id_seq', 1, false);
            public       thousanddays    false    182            |          0    16526    thoureport_storederrormessage 
   TABLE DATA               :   COPY thoureport_storederrormessage (id, text) FROM stdin;
    public       thousanddays    false    179    2209   &      �           0    0 $   thoureport_storederrormessage_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('thoureport_storederrormessage_id_seq', 1, false);
            public       thousanddays    false    178            �          0    16576    thoureport_storedresponse 
   TABLE DATA               <   COPY thoureport_storedresponse (id, text, code) FROM stdin;
    public       thousanddays    false    185    2209   C      �           0    0     thoureport_storedresponse_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('thoureport_storedresponse_id_seq', 6, true);
            public       thousanddays    false    184            ~          0    16537    thoureport_storedsms 
   TABLE DATA               D   COPY thoureport_storedsms (id, message, sender, "when") FROM stdin;
    public       thousanddays    false    181    2209          �           0    0    thoureport_storedsms_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('thoureport_storedsms_id_seq', 35, true);
            public       thousanddays    false    180            �          0    16605    thousanddays_reports 
   TABLE DATA               =   COPY thousanddays_reports (indexcol, created_at) FROM stdin;
    public       thousanddays    false    191    2209   �"      �           0    0 !   thousanddays_reports_indexcol_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('thousanddays_reports_indexcol_seq', 1, false);
            public       thousanddays    false    190            �          0    16648    timothyreports 
   TABLE DATA               `   COPY timothyreports (indexcol, timfield_timothy, timfield_kaboya, timfield_kalimba) FROM stdin;
    public       thousanddays    false    201    2209   �"      �           0    0    timothyreports_indexcol_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('timothyreports_indexcol_seq', 1, false);
            public       thousanddays    false    200            �           2606    16435    auth_group_name_key 
   CONSTRAINT     R   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         thousanddays    false    168    168    2210            �           2606    16420 1   auth_group_permissions_group_id_permission_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);
 r   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_key;
       public         thousanddays    false    166    166    166    2210            �           2606    16418    auth_group_permissions_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         thousanddays    false    166    166    2210            �           2606    16433    auth_group_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         thousanddays    false    168    168    2210            �           2606    16410 ,   auth_permission_content_type_id_codename_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);
 f   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_key;
       public         thousanddays    false    164    164    164    2210            �           2606    16408    auth_permission_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         thousanddays    false    164    164    2210            �           2606    16448    auth_user_groups_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         thousanddays    false    170    170    2210            �           2606    16450 %   auth_user_groups_user_id_group_id_key 
   CONSTRAINT     w   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);
 `   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_key;
       public         thousanddays    false    170    170    170    2210            �           2606    16478    auth_user_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         thousanddays    false    174    174    2210            �           2606    16463    auth_user_user_permissions_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         thousanddays    false    172    172    2210            �           2606    16465 4   auth_user_user_permissions_user_id_permission_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);
 y   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_key;
       public         thousanddays    false    172    172    172    2210            �           2606    16480    auth_user_username_key 
   CONSTRAINT     X   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         thousanddays    false    174    174    2210            �           2606    16400    django_admin_log_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         thousanddays    false    162    162    2210            �           2606    16505 '   django_content_type_app_label_model_key 
   CONSTRAINT     {   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);
 e   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_key;
       public         thousanddays    false    176    176    176    2210            �           2606    16503    django_content_type_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         thousanddays    false    176    176    2210            �           2606    16523    django_session_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         thousanddays    false    177    177    2210            �           2606    16553    thoureport_smserror_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY thoureport_smserror
    ADD CONSTRAINT thoureport_smserror_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.thoureport_smserror DROP CONSTRAINT thoureport_smserror_pkey;
       public         thousanddays    false    183    183    2210            �           2606    16534 "   thoureport_storederrormessage_pkey 
   CONSTRAINT     w   ALTER TABLE ONLY thoureport_storederrormessage
    ADD CONSTRAINT thoureport_storederrormessage_pkey PRIMARY KEY (id);
 j   ALTER TABLE ONLY public.thoureport_storederrormessage DROP CONSTRAINT thoureport_storederrormessage_pkey;
       public         thousanddays    false    179    179    2210            �           2606    16584    thoureport_storedresponse_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY thoureport_storedresponse
    ADD CONSTRAINT thoureport_storedresponse_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.thoureport_storedresponse DROP CONSTRAINT thoureport_storedresponse_pkey;
       public         thousanddays    false    185    185    2210            �           2606    16545    thoureport_storedsms_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY thoureport_storedsms
    ADD CONSTRAINT thoureport_storedsms_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.thoureport_storedsms DROP CONSTRAINT thoureport_storedsms_pkey;
       public         thousanddays    false    181    181    2210            �           1259    16559    auth_group_name_like    INDEX     X   CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);
 (   DROP INDEX public.auth_group_name_like;
       public         thousanddays    false    168    2210            �           1259    16557    auth_group_permissions_group_id    INDEX     _   CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);
 3   DROP INDEX public.auth_group_permissions_group_id;
       public         thousanddays    false    166    2210            �           1259    16558 $   auth_group_permissions_permission_id    INDEX     i   CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);
 8   DROP INDEX public.auth_group_permissions_permission_id;
       public         thousanddays    false    166    2210            �           1259    16556    auth_permission_content_type_id    INDEX     _   CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);
 3   DROP INDEX public.auth_permission_content_type_id;
       public         thousanddays    false    164    2210            �           1259    16561    auth_user_groups_group_id    INDEX     S   CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);
 -   DROP INDEX public.auth_user_groups_group_id;
       public         thousanddays    false    170    2210            �           1259    16560    auth_user_groups_user_id    INDEX     Q   CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);
 ,   DROP INDEX public.auth_user_groups_user_id;
       public         thousanddays    false    170    2210            �           1259    16563 (   auth_user_user_permissions_permission_id    INDEX     q   CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);
 <   DROP INDEX public.auth_user_user_permissions_permission_id;
       public         thousanddays    false    172    2210            �           1259    16562 "   auth_user_user_permissions_user_id    INDEX     e   CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);
 6   DROP INDEX public.auth_user_user_permissions_user_id;
       public         thousanddays    false    172    2210            �           1259    16564    auth_user_username_like    INDEX     ^   CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);
 +   DROP INDEX public.auth_user_username_like;
       public         thousanddays    false    174    2210            �           1259    16555     django_admin_log_content_type_id    INDEX     a   CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);
 4   DROP INDEX public.django_admin_log_content_type_id;
       public         thousanddays    false    162    2210            �           1259    16554    django_admin_log_user_id    INDEX     Q   CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);
 ,   DROP INDEX public.django_admin_log_user_id;
       public         thousanddays    false    162    2210            �           1259    16566    django_session_expire_date    INDEX     U   CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);
 .   DROP INDEX public.django_session_expire_date;
       public         thousanddays    false    177    2210            �           1259    16565    django_session_session_key_like    INDEX     n   CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);
 3   DROP INDEX public.django_session_session_key_like;
       public         thousanddays    false    177    2210            �           2606    16421 )   auth_group_permissions_permission_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_permission_id_fkey;
       public       thousanddays    false    166    164    1998    2210                       2606    16451    auth_user_groups_group_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 Y   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_fkey;
       public       thousanddays    false    170    168    2009    2210                       2606    16466 -   auth_user_user_permissions_permission_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_permission_id_fkey;
       public       thousanddays    false    172    1998    164    2210            �           2606    16506     content_type_id_refs_id_93d2d1f8    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT content_type_id_refs_id_93d2d1f8 FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 [   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT content_type_id_refs_id_93d2d1f8;
       public       thousanddays    false    2030    162    176    2210            �           2606    16511     content_type_id_refs_id_d043b34a    FK CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 Z   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT content_type_id_refs_id_d043b34a;
       public       thousanddays    false    2030    176    164    2210                        2606    16436    group_id_refs_id_f4b32aac    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 Z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT group_id_refs_id_f4b32aac;
       public       thousanddays    false    168    166    2009    2210                       2606    16486    user_id_refs_id_40c41112    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 S   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT user_id_refs_id_40c41112;
       public       thousanddays    false    2023    174    170    2210                       2606    16491    user_id_refs_id_4dc23c39    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 ]   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT user_id_refs_id_4dc23c39;
       public       thousanddays    false    174    172    2023    2210            �           2606    16481    user_id_refs_id_c0d12874    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT user_id_refs_id_c0d12874 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 S   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT user_id_refs_id_c0d12874;
       public       thousanddays    false    162    2023    174    2210            q      x������ � �      o      x������ � �      m   <  x�m�K�� @��9���o�s��FQ�2�� ]��C��ul���)�g����<��hs���"Ŀ!�!����f�jF�T�.���T�"ݵ���߭*Zkz�e �	;P5c�Mر�Wg��h�8�a��|��D\�)(I����k'���})i���	P�=�=mi~���l�׮E%�zg@v�u������O<����L�u�����H��6Qo�P�1���N���Ŕ�1bP-sR0k+�11e���}�o���Y'�I�����`Y]ȑ�	�Ņ�ίv���x-�oVߞ���@k�JY{��Z�6R�~� �T�t.      w   �   x�3�,H�NI3�/�H425S14200P�N7�.tt*�4�U)-I7�ү5���(s�M��Ou�0�֯*�ȳ�w����LN	,��϶�4204�50�52T04�21�21�32742�60�,�,J-K�KN�䄱�K�JӁR%x�r��qqq .a      s      x������ � �      u      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      k      x������ � �      y   �   x�e�K� ��)8A����.�D�� �l���I�Ru�ߌ�s_E��!�XyE�@"	^�s�>�t`��(���׈7�J�����Vʜ͉ԬG�(mW��-��Xhpl�,�Xl�E���H���C��awnB�J7����O�� c      z   1  x�]�Mo�0 �����M)-_7�)�5*�����G+�8�_?�,��o�<���JB�umUWe����WU�#F�%"�$�[L/��(7��7��\�u2&��^��â�C�Pm��6=�*+�^~J�j�(i�"��{��7z�bE˺`���E� 0��c��G�oZ�qm�h$um��S	n�V�8�x��_�F_��HDl���ⱀ2ު5�月�:�z^��2H1't�ѩ1E,�cV��v��E�g�`%��,OuU�f�#!�]�}��̧�ES��~�G�oky/���0��u�      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �   .   x�3����N,��0�e�Y�Z����
���L*O��D���qqq ��      �      x������ � �      �      x������ � �      |      x������ � �      �   �   x���M
�0���)� `��{A((h��J�f��6)I[=�����-ua�R��z3��|>�[k,��� ,J�t)%y��Xa"I�M������Ia
9�� ��Vk�F3�M����#��uOb�S����G�-:"K�Vb]�Hс�;�؁Ule�j('}���!��ǫЪ��A����������L��      ~   �  x����NSAǯ�Oq�����9w
!��n*)��A��g3�|g� BK�Q��E���fv���ճ� ���P�@�;�J��(=�P8�_|ڭ�Ȅ������`��z�ll�ʥ�;Dˢ%Y�	�s�Խ8쎦��ׅb>�<Y�����g{�Kd��:*�N���P�ZA���g�%I!������~�=hTՂ�_������ɢX6m~{�=;���͒r���yz�퀔�$�BҚ�� ճ�$��蔦�[�.:SL
)~���枊q�L�[������l��l���r4He��,\b�ل��iDjT'P)�Ϗ{{�dK�SFx�g��V�IG{̓|�k�|�U�������`81��+E���U�HlPZ����1 r���� �A���� m+C"_��be�7���q'�[?����&��De���1��H@b�M�b��[8d��%���7�t�Z�phy�p4�^�M����d蛅�����l�}����ѧΛ$>9)f���~m��pu�8���tݣuI���VmO�z��/C�oʥ�G�v��U�����m�w�f�E`Op�[�!�����:Fo������7 ���k�3�2��fJi�/��A�d�����t�q'� �Cr]*��9���8�L~�      �      x������ � �      �      x������ � �     