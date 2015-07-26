module.exports = function(grunt) {

    /**
     * Initialize grunt
     */
    grunt.initConfig({
        config: grunt.file.readJSON('build.json'),
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
                files: [{
                    expand: true,
                    cwd: '<%= config.src_dir %>',
                    src: ['**/*js'],
                    dest: '<%= config.build_dir %>/app/static/'
                }]
            }
        },

        clean: {
            js: ["<%= config.build_dir %>/**"]
        },

        copy: {
            lib: {
                files: [{
                    expand: true,
                    flatten: true,
                    cwd: 'bower_components/',
                    src: ['**/*min.js'],
                    dest: '<%= config.build_dir %>/app/static/lib/js'
                }]
            },
            libcss: {
                files: [{
                    expand: true,
                    flatten: true,
                    cwd: 'bower_components/',
                    src: ['**/*.css'],
                    dest: '<%= config.build_dir %>/app/static/lib/css'
                }]
            },
            libfonts: {
                files: [{
                    expand: true,
                    flatten: true,
                    cwd: 'bower_components/',
                    src: ['**/*.woff*', '**/*.ttf', '**/*.svg', '**/*.eot'],
                    dest: '<%= config.build_dir %>/app/static/lib/fonts'
                }]
            },
            assets: {
                files: [{
                    expand: true,
                    flatten: true,
                    cwd: 'src/assets',
                    src: ['**'],
                    dest: '<%= config.build_dir %>/app/static/assets'
                }]
            },
            server: {
                files: [{
                    expand: true,
                    cwd: '<%= config.src_dir %>/server',
                    src: ['**'],
                    dest: '<%= config.build_dir %>/'
                }]
            }
        },

        less: {
            css: {

                options: {
                    banner: '<%= banner %>',
                    plugins: [
                        new(require('less-plugin-autoprefix'))({
                            browsers: ["last 2 versions"]
                        }),
                        new(require('less-plugin-clean-css'))({
                            advanced: true
                        })
                    ],
                    modifyVars: {
                        imgPath: '"http://localhost:5000/static/assets"',
                        bgColor: 'red'
                    }
                },
                files: [{
                    expand: true,
                    flatten: true,
                    cwd: '<%= config.src_dir %>/css',
                    src: ['**/*'],
                    dest: '<%= config.build_dir %>/app/static/css'
                }]
            }
        },
        watch: {
            scripts: {
                files: ['<%= config.src_dir %>/**/**'],
                tasks: ['build'],
                options: {
                    spawn: false,
                },
            },
        },

        //shell command to start server
        shell: {
            run: {
                options: {
                    stdout: true
                },
                command: ['cd bin', 'python run.py'].join(';')
            },
            setup: {
                options: {
                    stdout: true
                },
                command: ['cd bin', 'python setup.py'].join(';')
            }
        },

        //runs both the python server and watches the file change
        concurrent: {
            watch: {
                tasks: ['shell:run', 'watch'],
                options: {
                    logConcurrentOutput: true
                }
            }

        }

    });

    grunt.loadNpmTasks('grunt-shell');
    grunt.loadNpmTasks('grunt-sync');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-concurrent');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-newer');

    grunt.registerTask('wtch', ['build', "concurrent:watch"]);
    grunt.registerTask('build', ['newer:uglify', 'newer:copy', "newer:less"]);
    grunt.registerTask('default', ['build']);
    grunt.registerTask('cln', ['clean']);

    grunt.registerTask('run', ['shell:run']);
    grunt.registerTask('migrate', []);
    grunt.registerTask('setup', ["shell:setup"])
};