/* globals angular*/

export default angular.module('homeCtrls', [])
  .controller('homeCtrl', [
    '$scope', (scope) => {
      scope.startHeaderParticle = () => {
        scope.particles('particles-js', {
          particles: {
            number: {
              value: 50,
              density: { enable: true, value_area: 3000 },
            },
            color: { value: '#004400' },
            shape: {
              type: 'polygon',
              stroke: { width: 0, color: '#000' },
              polygon: { nb_sides: 6 },
            },
            opacity: {
              value: 0.5,
              random: true,
              anim: {
                enable: true,
                speed: 1,
                opacity_min: 0.1,
                sync: false,
              },
            },
            size: {
              value: 150,
              random: true,
              anim: {
                enable: true,
                speed: 10,
                size_min: 40,
                sync: false,
              },
            },
            line_linked: { enable: false },
            move: {
              enable: true,
              speed: 8,
              direction: 'none',
              random: true,
              straight: false,
              out_mode: 'bounce',
              bounce: false,
              attract: { enable: false },
            },
          },
          interactivity: {
            events: {
              onhover: { enable: false },
              onclick: { enable: false },
            },
          },
          retina_detect: true,
        });
      };
    },
  ]);
