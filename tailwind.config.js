module.exports = {
  content: ["./index.html", "./support-technique-seance-03.html", "./tools/*.py"],
  theme: {
    extend: {
      boxShadow: {
        neo: "8px 8px 0 #0f172a",
        "neo-sm": "4px 4px 0 #0f172a",
        glow: "0 18px 50px rgba(79, 70, 229, .16)",
      },
      colors: {
        ink: "#0f172a",
        denemBlue: "#2563eb",
        denemViolet: "#7c3aed",
        denemCyan: "#06b6d4",
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"],
        mono: ["JetBrains Mono", "ui-monospace", "SFMono-Regular", "monospace"],
      },
    },
  },
  plugins: [],
};

