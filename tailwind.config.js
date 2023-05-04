/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {
    extend: {  colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'deeppurp': '#393646',
      'lightdeeppurp': '#4F4557',
      'alternativepurp': '#393b40'
      },
    },
  },
  plugins: [],
}

