# Hosting a Public Webpage with [Tachyon](https://store.particle.io/products/tachyon-5g-single-board-computer)

A powerful single-board computer with 5G out of the box can enable a bunch of useful remote monitoring projects. But once your sensors are wired up and your code is running, you’ll need a way to interact with the device while it’s deployed.

This project demonstrates how to host a publicly available website directly on a Tachyon device using a [Cloudflare tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/).

For example, you can connect a USB camera to the Tachyon, run a Flask server, and expose a live video feed over the internet. [The Flockr project](https://github.com/epietrowicz/flockr-app-2.0) uses this exact setup.

## Features
- Host a Flask-based webpage directly from a Tachyon device
- Expose services to the public internet securely with Cloudflare tunnels
- Configure your own domain name (via providers like Namecheap)
- Run services in Particle for Linux containers for easy deployment
- Extendable for any remote monitoring project (cameras, sensors, dashboards, etc.)

## Prerequisites

Before starting, make sure you have:
- [A Tachyon SBC](https://store.particle.io/products/tachyon-5g-single-board-computer) set up and running
- [Particle for Linux v0.20.2+](https://developer.particle.io/linux/)
- [Particle CLI v3.42.1+](https://github.com/particle-iot/particle-cli)
- A registered domain (e.g., through [Namecheap](https://www.namecheap.com/))
- A [Cloudflare](https://www.cloudflare.com/) account (free tier works fine)
