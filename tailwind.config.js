/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'templates/**/*.{html,js}',
    'templates/*.{html,js}',
    'static/**/*.{html,js}',
  ],
  theme: {
    extend: {
      backgroundImage: {
        'hero': "url('../../images/Rectangle 29.jpg')",
        'footer-texture': "url('/img/footer-texture.png')",
      }
    },
    screens: {
      'mspp': '310px',
      'smpl': '424px',
      'sm': '640px',
      'md': '768px',
      'mdpl': '942px',
      'lg': '1024px',
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
  plugins: [],
}
