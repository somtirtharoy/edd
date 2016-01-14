module.exports = function(grunt) {

    grunt.loadNpmTasks('grunt-typescript');
    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-exec');
    grunt.loadNpmTasks('grunt-insert-timestamp');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.initConfig({
    	clean: {
    		build: ["./typescript/build/"]
        },
        typescript: {
            dev: {
                src: ['./typescript/build/*.ts'],
                dest: './typescript/build/',
                options: {
                    rootDir: './typescript/build/',
                    target: 'es5',
                    declaration: false,
                    sourceMap: true,
                    removeComments: false,
                }
            },
            prod: {
                src: ['./typescript/build/*.ts'],
                dest: './typescript/build/',
                options: {
                    rootDir: './typescript/build/',
                    target: 'es5',
                    declaration: false,
                    sourceMap: false,
                    removeComments: true,
                }
            }
        },
        uglify: {
            options: {
                mangle: false
            },
            prod: {
                files: [{
                    expand: true,
                    cwd: './typescript/build/',
                    src: '**/*.js',
                    dest: './typescript/build/'
                }]
            }
        },
        insert_timestamp: {
            js: {
                options: {
                    prepend: false,
                    append: true,
                    // Uses default output of `Date()`
                    format: false,
                    template: '// JS compiled on: {timestamp}  ',
                    insertNewlines: true
                },
                files: [{
                    // Use dynamic extend name
                    expand: true,
                    // Source dir
                    cwd: './typescript/build/',
                    // Match files
                    src: ['**/*.js'],
                    // Output files
                    dest: './typescript/build/',
                    ext: '.js'
                }]
            }
        },
        copy: {
            prep: {
                cwd: './typescript/src/',    // set working folder / root to copy
                src: '**/*',                 // copy all files and subfolders
                dest: './typescript/build/', // destination folder
                expand: true                 // required when using cwd
            },
            mergeDev: {
                cwd: './typescript/build/',
                src: '**/*',
                dest: './main/static/main/js/',
                expand: true
            },
            mergeProd: {
                cwd: './typescript/build/',
                src: '**/*.js',
                dest: './main/static/main/js/',
                expand: true
            }
        },
        exec: {
            collect: {
                command: './manage.py collectstatic',
                stdout: true
            }
        },
        watch: {
            scripts: {
                files: ['./typescript/src/*.ts'],                 // the watched files
                tasks: ["clean:build", "copy:prep", "typescript:dev", "insert_timestamp:js", "copy:mergeDev", "exec:collect"],  // the task(s) to run
                options: {
                    spawn: false // makes the watch task faster
                }
            }
        }
    });


    var production = grunt.option('production');
    var watch = grunt.option('watch');

    if (production) {
        // One-time production build
        grunt.registerTask('default', ["clean:build", "copy:prep", "typescript:prod", "uglify:prod", "copy:mergeProd", "exec:collect"]);
    } else if (watch) {
        // Dev build and watch for changes
        grunt.registerTask('default', ["clean:build", "copy:prep", "typescript:dev", "insert_timestamp:js", "copy:mergeDev", "exec:collect", 'watch']);
    } else {
        // Standard one-time dev build
        grunt.registerTask('default', ["clean:build", "copy:prep", "typescript:dev", "insert_timestamp:js", "copy:mergeDev", "exec:collect"]);
    }
};



