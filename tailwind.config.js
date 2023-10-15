/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./static/**/*.{html,js}",
    "./templates/**/*.{html,js}",
  ],
  theme: {
    screens: {
      sm: "576px",
      // => @media (min-width: 640px) { ... }

      md: "768px",
      // => @media (min-width: 768px) { ... }

      lg: "992px",
      // => @media (min-width: 1024px) { ... }

      xl: "1200px",
      // => @media (min-width: 1280px) { ... }

      "2xl": "1400px",
      // => @media (min-width: 1536px) { ... }
    },
    extend: {
      fontFamily: {
        perker: ["Permanent Marker", "cursive"],
      },
    },
  },
  corePlugins: {
    container: false,
  },
  plugins: [
    function ({ addComponents }) {
      addComponents({
        ".container": {
          maxWidth: "100%",
          marginLeft: "auto",
          marginRight: "auto",
          paddingLeft: "1.5rem",
          paddingRight: "1.5rem",
          "@screen sm": {
            maxWidth: "540px",
            paddingLeft: "1rem",
            paddingRight: "1rem",
          },
          "@screen md": {
            maxWidth: "720px",
          },
          "@screen lg": {
            maxWidth: "960px",
          },
          "@screen xl": {
            maxWidth: "1140px",
          },
          "@screen 2xl": {
            maxWidth: "1320px",
          },
        },
      });
    },
  ],
};
