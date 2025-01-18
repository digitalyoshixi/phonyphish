import type { NextConfig } from "next";
const withPWA = require('next-pwa');

const nextConfig: NextConfig = {
  reactStrictMode: true,      // Enable React strict mode for improved error handling
  swcMinify: true,            // Enable SWC minification for improved performance
  compiler: {
        removeConsole: process.env.NODE_ENV !== "development"     // Remove console.log in production
    }
  /* config options here */
};

export default withPWA({
  dest: "public",         // destination directory for the PWA files
  disable: process.env.NODE_ENV === "development",        // disable PWA in the development environment
  register: true,         // register the PWA service worker
  skipWaiting: true,      // skip waiting for service worker activation
})(nextConfig);

