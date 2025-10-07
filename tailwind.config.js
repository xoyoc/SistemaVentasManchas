/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.{html,js}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/templates/**/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'manchas-yellow': '#FFD700',
        'manchas-black': '#000000',
      },
    },
  },
  plugins: [],
  // Importante: Asegurarse de que todas las clases estén disponibles
  safelist: [
    'bg-yellow-400',
    'bg-yellow-500',
    'bg-red-500',
    'bg-red-600',
    'bg-green-500',
    'bg-green-600',
    'bg-blue-500',
    'bg-blue-600',
    'text-yellow-400',
    'text-yellow-600',
    'border-yellow-400',
    'hover:bg-yellow-500',
    'hover:bg-red-600',
    'hover:bg-green-600',
    'hover:bg-blue-600',
  ]
}