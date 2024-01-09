/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'poppins': ['Poppins', 'sans-serif'],
        'pixel' : ['Press+Start+2P', 'system-ui']
      },
      colors: {
        main: '#725DEF'
      }
    },
  },
  plugins: [],
}

