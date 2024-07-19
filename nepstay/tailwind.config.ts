import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors:
      {
        "nepal": "#8B4513",
        "nepal-dark": "#654321",
        "nepal-light": "#A0522D",
        "nepal-lighter": "#CD853F",
        "nepal-lightest": "#DEB887",
      },
    },
  },
  plugins: [],
};
export default config;
