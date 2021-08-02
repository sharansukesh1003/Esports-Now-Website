var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0],
    offset: 'bottom-in-view',
    onBeforePageLoad: function(){
      $('.loader').show();
    },
    onAfterPageLoad: function(){
     $('.loader').hide();
    },
  })