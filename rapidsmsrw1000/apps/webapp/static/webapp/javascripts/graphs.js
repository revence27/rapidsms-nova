$(function()
{
  var thr = new ThousandQueries(document.location);
  f1(thr);
  f2(thr);
});

var f1  =        function (thr) {

        $('#lmpgraph').highcharts({
            chart: {
                type: 'column'
            },
            
            xAxis: {
                categories: [
                    '1',
                    '2',
                    '3',
                    '4',
                    '5',
                    '6',
                    '7',
                    '8',
                    '9'
                    
                ]
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Pregnancies Reported'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y:.1f} </b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                name: 'LMP Known in terms of months',
                data: thr.lmpData([123, 111, 91, 87, 72, 64, 60, 21, 02])
    
            }]
        });
    };

var f2 = function (thr) {
    $('#monthlyavggrph').highcharts({
        
        xAxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },
        yAxis: {
            title: {
                text: 'Pregnancies Confirmed'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: ''
        },
        
        series: [{
            name: 'Pregnancies Per Month',
            data: thr.pregsPerMonth([70, 69, 95, 145, 102, 25, 52, 65, 33, 83, 39, 96])
        }]
    });
};
