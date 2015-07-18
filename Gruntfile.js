module.exports = function(grunt) {

  /**
   * Initialize grunt
   */
  grunt.initConfig({
    config : grunt.file.readJSON('build.json'),
    pkg: grunt.file.readJSON('package.json'),
    /**
     * Set banner
     */
    banner: '/**\n' +
    '<%= pkg.title %> - <%= pkg.version %>\n' +
    '<%= pkg.homepage %>\n' +
    'Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>\n' +
    'License: <%= pkg.license %>\n' +
    '*/\n',
    /**
     * Minify
     * @github.com/gruntjs/grunt-contrib-uglify
     */
    uglify: {

      // Uglify options
      options: {
        banner: '<%= banner %>',
         mangle: false
      },

      build: {
        files: [
        {

          mangle:false,
          expand: true,
          cwd: 'src',
          src: ['!**/controller/*js','**/*js'],
          dest: 'app/static/'
        }]
      }
    },

    clean: {
      js: ["app/static/**"]
    },

      copy: {
            lib: {
                files: [{
                    expand: true,
                    flatten: true,
                    cwd: 'bower_components/',
                    src: ['**/*min.js'],
                    dest: 'app/static/lib/js'
                }]
            },
            libcss : {
                files: [{
                    expand: true,
                    flatten: true,
                    cwd: 'bower_components/',
                    src: ['**/*.css'],
                    dest: 'app/static/lib/css'
                }]
            },
            assets:{
                files: [{
                    expand: true,
                    flatten: true,
                    cwd: 'src/assets',
                    src: ['**'],
                    dest: 'app/static/assets'
                }]
            },
            css : {
               files: [{
                    expand: true,
                    flatten: true,
                    cwd: 'src/css',
                    src: ['**/*css'],
                    dest: 'app/static/css'
                }]
            }
      }

  });


grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-contrib-copy');
grunt.loadNpmTasks('grunt-contrib-clean');

    grunt.registerTask('default', ['clean','uglify','copy']);
};