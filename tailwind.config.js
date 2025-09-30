/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'macy-red': '#E22D34',
        'macy-blue': '#0C2340',
      },
    },
  },
  plugins: [],
}