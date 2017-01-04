var vex = require('vex-js');
vex.registerPlugin(require('vex-dialog'));
vex.defaultOptions.className = 'vex-theme-os';

vex.dialog.confirm({
  message: 'Are you absolutely sure you want to destroy the alien planet?',
  callback: function (value) {
    if (value) {
      console.log('Successfully destroyed the planet.')
    } else {
      console.log('Chicken.')
    }
  }
})
