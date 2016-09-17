/// <reference path="../typings/d3/d3.d.ts"/>;
/// <reference path="GraphHelperMethods.ts" />
/// <reference path="StudyGraphingHelperMethods.ts" />

var StudyDGraphing:any;

declare var createMultiLineGraph;
declare var createGroupedBarGraph;

StudyDGraphing = {

	Setup:function(graphdiv) {

		if (graphdiv) {
			this.graphDiv = $("#" + graphdiv);
		} else {
			this.graphDiv = $("#graphDiv");
        }
	},

	clearAllSets:function() {
        $('.tooMuchData').remove();
        var divs =  this.graphDiv.siblings();

        if ($(divs[1]).find( "svg" ).length == 0 ){
             d3.selectAll("svg").remove();
        }
        else {
            for (var div = 1; div < divs.length; div++) {
                $(divs[div]).find("svg").remove()
            }
        }
	},

	addNewSet:function(newSet, type) {

        var buttonArr = StudyHelper.getButtonElement(this.graphDiv),
            selector = StudyHelper.getSelectorElement(this.graphDiv),
            type = StudyHelper.measurementType(type),
            buttons = {
                'line': buttonArr[0],
                'bar-empty': buttonArr[1],
                'bar-time': buttonArr[2],
                'bar-line': buttonArr[3],
                'bar-measurement': buttonArr[4]
            },
            selectors = {
                'line': selector[1],
                'bar-time': selector[2],
                'bar-line': selector[3],
                'bar-measurement': selector[4]
            };

        /**
         * display grouped bar chart by measurement if most of the measurement types are protocol
         *  currently commented out because this is buggy
        **/
        //StudyHelper.showProteomicGraph(type, selectors, 'bar-measurement', buttons);

        //line chart
        $(buttons['line']).click(function(event) {
            event.preventDefault();
            StudyHelper.displayGraph(selectors, 'line');
            $('label.btn').removeClass('active');
            $(this).addClass('active');

            //hide graph option buttons
            $(buttons['bar-time']).addClass('hidden');
            $(buttons['bar-line']).addClass('hidden');
            $(buttons['bar-measurement']).addClass('hidden');
            return false
        });

        // when user clicks bar button, show option buttons
        $(buttons['bar-empty']).click(function(event){
            event.preventDefault();
            $(buttons['bar-time']).removeClass('hidden');
            $(buttons['bar-line']).removeClass('hidden');
            $(buttons['bar-measurement']).removeClass('hidden');
            $('label.btn').removeClass('active');
            $(this).addClass('active');
            return false
        });

        //bar chart grouped by time
        $(buttons['bar-time']).click(function(event) {
            var rects = d3.selectAll('.barTime rect')[0];
            StudyHelper.buttonEventHandler(newSet, event, rects, 'bar-time', selectors, buttonArr);
        });

        //bar chart grouped by line name
        $(buttons['bar-line']).click(function(event) {
            var rects = d3.selectAll('.barAssay rect')[0];
            StudyHelper.buttonEventHandler(newSet, event, rects, 'bar-line', selectors, buttonArr);
        });

        //bar chart grouped by measurement
        $(buttons['bar-measurement']).click(function(event) {
            var rects = d3.selectAll('.barMeasurement rect')[0];
            StudyHelper.buttonEventHandler(newSet, event, rects, 'bar-measurement', selectors, buttonArr);
        });

        var barAssayObj  = GraphHelperMethods.sortBarData(newSet);

        //data for graphs
        var graphSet = {
            barAssayObj: GraphHelperMethods.sortBarData(newSet),
            create_x_axis: GraphHelperMethods.createXAxis,
            create_right_y_axis: GraphHelperMethods.createRightYAxis,
            create_y_axis: GraphHelperMethods.createLeftYAxis,
            x_axis: GraphHelperMethods.make_x_axis,
            y_axis: GraphHelperMethods.make_right_y_axis,
            individualData: newSet,
            assayMeasurements: barAssayObj,
            width: 750,
            height: 220
        };

        //hide y-axis check box event handler
        $('.linechart .checkbox').click(function() {
            StudyHelper.toggleLine('.linechart', graphSet, selector);
        });

        $('.timeBar .checkbox').click(function() {
            StudyHelper.toggle('.timeBar', graphSet, selector[2], 'x');
        });
        $('.barAssay .checkbox').click(function() {
            StudyHelper.toggle('.barAssay', graphSet, selector[3], 'name');
        });
        $('.groupedMeasurement .checkbox').click(function() {
            StudyHelper.toggle('.groupedMeasurement', graphSet, selector[4], 'measurement');
        });

        //render different graphs first checking if the hide y-axis checkbox is checked.
        StudyHelper.isCheckedLine('.timeBar', graphSet, selector);
        StudyHelper.isChecked('.timeBar', graphSet, selector[2], 'x');
        StudyHelper.isChecked('.barAssay', graphSet, selector[3], 'name');
        StudyHelper.isChecked('.groupedMeasurement', graphSet, selector[4], 'measurement');

		if (!newSet.label) {
			$('#debug').text('Failed to fetch series.');
			return;
		}
	},

};