window.tictactoe = (function(d3, _){
  'use strict';

  function getPlayerSymbol(mark) {
    if (mark === 1) {
      return 'X';
    } else if (mark === -1){
      return 'O';
    }
  }

  function TicTacToe(selector, options) {
    var margin = { top: 50, right: 0, bottom: 100, left: 30 },
      width = 250 - margin.left - margin.right,
      height = 370 - margin.top - margin.bottom,
      gridSize = Math.floor(width / 3),
      container = document.querySelector(selector),
      data = [null, null, null, null, null, null, null, null, null],
      currentPlayer = _.reduce(data, function(memo, num){ return memo + num; }, 0) * -1 || 1;

    var svg = d3.select(container).append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

    var cells = svg.selectAll('.cell-container')
      .data(data);

    var cellGroups = cells.enter().append('g')
      .attr('class', 'cell-container')
      .attr('transform', function(d, i) {
        return 'translate(' + (i % 3 * gridSize) + ',' + Math.floor(i / 3) * gridSize + ')'
      })
      .on('click', function(d, i) {
        if (d)
          return;

        data[i] = currentPlayer;
        currentPlayer *= -1;
        updateLabels(data);
      });

    cellGroups
      .append('rect')
      .attr('rx', 4)
      .attr('ry', 4)
      .attr('class', 'cell bordered')
      .attr('width', gridSize)
      .attr('height', gridSize)
      .style('fill', 'steelblue');

    cellGroups
      .append('text')
      .attr('class', 'player-symbol')
      .attr('x', gridSize/2)
      .attr('y', gridSize/2 + 10) // MAGIC
      .attr('text-anchor', 'middle');

    function updateLabels(data) {
      svg.selectAll('.cell-container')
        .data(data)
        .select('text')
        .text(getPlayerSymbol);
    }

    updateLabels(data);
  }

  return {
    'TicTacToe': TicTacToe
  };
}(window.d3, window._));
