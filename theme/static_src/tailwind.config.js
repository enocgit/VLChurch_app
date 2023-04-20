/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        '../../**/*.py'
    ],
    theme: {
        extend: {
          backgroundImage: {
            'hero': "url('/static/images/hero-bg.jpg')",
            'footer-texture': "url('/img/footer-texture.png')",
          }
        },
        screens: {
          'mspp': '310px',
          'smpl': '424px',
          'smp2': '462px',
          'smpp': '529px',
          'sm': '640px',
          // 'smpp': '767px',
          'md': '768px',
          'md2': '900px',
          'mdpl': '942px',
          'lg': '1024px',
          'lg2': '1184px',
          'xl': '1280px',
          '2xl': '1536px',
        },
        fontFamily: {
          'fantasy': ['"Akaya Kanadaka"', 'fantasy'],
          'serif': ['"Abhaya Libre"', 'serif'],
          'sans': ['Actor', 'sans-serif'],
          'sans-head': ['Inter', 'sans-serif'],
          'cursive': ['Lobster', 'cursive']
        },
        // textColor: {
        //   'primary-brown': '#462D1A',
        // }
    
      },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        require('flowbite/plugin')
    ],
}
