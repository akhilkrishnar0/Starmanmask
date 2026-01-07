# Starmanmask 🌟  
**Manually mask stars in galaxy FITS images**

Starmanmask is a Python package designed for **manual, science-grade masking of stars and compact sources** in galaxy FITS images.  
It provides an **interactive ellipse-based GUI** to visually select stars and then apply those masks consistently to the data.

This tool is especially useful for:
- Low Surface Brightness (LSB) galaxy studies
- Extended galaxy structure analysis
- Preparing images for surface-brightness profile fitting
- Situations where automatic star masks fail or over-mask galaxy light

---

## ✨ Features

- Interactive ellipse drawing on FITS images
- WCS-aware (RA/DEC in degrees)
- Stores ellipse parameters in a CSV table
- Converts ellipse sizes to arcseconds
- Applies masks to FITS images
- Side-by-side visualization: **original vs masked**
- Saves masked FITS images for downstream analysis

---

## 📦 Installation

Clone the repository and install locally:

```bash
git clone https://github.com/akhilkrishnar0/Starmanmask.git
cd Starmanmask
pip install -e .

