/* globals angular, Event*/

export default angular.module('homeCtrls', [])
  .controller('homeCtrl', [
    '$scope', '$window', (scope, wind) => {
      scope.particlesLoaded = false;
      scope.startHeaderParticle = () => {
        scope.particles('particles-js', {
          particles: {
            number: {
              value: 10,
              density: { enable: false },
            },
            color: { value: '#3C65C2' },
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
              value: 50,
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
              out_mode: 'out',
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
        scope.particlesLoaded = true;
      };
      wind.addEventListener(
        'load', () => { scope.startHeaderParticle(); },
        {
          once: true,
          capture: false,
        }
      );
    },
  ]);
