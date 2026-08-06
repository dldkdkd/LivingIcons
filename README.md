# LivingIcons 

<p align="center">
  <img src="animated-settings-app-icon.gif" width="128" alt="LivingIcons icon">
</p>

<h3 align="center">Your Home Screen, alive.</h3>

<p align="center">
  Animate app icons, build complete themes, customize individual apps, and preview everything directly from Settings.
</p>

<p align="center">
  <a href="https://dldkdkd.github.io/LivingIcons/"><strong>Open the LivingIcons site</strong></a>
  ·
  <a href="sileo://source/https://dldkdkd.github.io/LivingIcons/"><strong>Add to Sileo</strong></a>
</p>

---

## LivingIcons Website

The full LivingIcons website is hosted through GitHub Pages:

**https://dldkdkd.github.io/LivingIcons/**

It includes:

- Animated icon previews
- Feature explanations
- Installation instructions
- Screenshots
- Package information
- Direct Sileo source link

<p align="center">
  <img src="assets/icons/com.apple.MobileSMS.gif" width="82" alt="Messages animated icon">
  <img src="assets/icons/com.apple.Preferences.gif" width="82" alt="Settings animated icon">
  <img src="assets/icons/com.apple.Maps.gif" width="82" alt="Maps animated icon">
  <img src="assets/icons/com.apple.camera.gif" width="82" alt="Camera animated icon">
  <img src="assets/icons/com.apple.weather.gif" width="82" alt="Weather animated icon">
  <img src="assets/icons/com.apple.Music.gif" width="82" alt="Music animated icon">
</p>

---

## LivingIcons

LivingIcons brings animated app icons to jailbroken iOS.

Assign GIF, APNG, PNG, or JPG artwork to installed apps, switch between full animation themes, adjust playback speed and looping, and preview animations directly inside the native Settings app.

### Features

- Animated Home Screen app icons
- GIF, APNG, PNG, and JPG support
- Per-app media assignments
- Per-app speed and loop controls
- Theme Manager
- Theme Studio
- Live previews in Settings
- Built-in animated Settings icon
- Installed-app search
- Image and GIF compression
- Bulk theme-management tools
- Notification badges remain above animations
- Native Settings preference pane
- Included starter animation theme
- Relaxin RootHide support
- Automatic `oldabi` dependency installation

### Theme location

Custom themes live at:

```text
/var/jb/var/mobile/Documents/LivingIcons/Themes/
```

Themes can be edited manually with Filza or managed from the LivingIcons Settings pane.

### Quick setup

1. Add the repository to Sileo:

   ```text
   https://dldkdkd.github.io/LivingIcons/
   ```

2. Install **LivingIcons**.
3. Respring.
4. Open:

   ```text
   Settings → LivingIcons
   ```

5. Select **Installed Apps** to assign an animation to one app.
6. Select **Themes** to activate a full animation pack.
7. Use **Reload LivingIcons** after editing theme files manually.

### Screenshots

<p align="center">
  <img src="assets/screenshots/IMG_4477_1785942728293.png" width="220" alt="LivingIcons screenshot">
  <img src="assets/screenshots/IMG_4480_1785944193246.png" width="220" alt="LivingIcons screenshot">
  <img src="assets/screenshots/IMG_4481_1785945216147.png" width="220" alt="LivingIcons screenshot">
</p>

---

## LivingIcons Dumper

LivingIcons Dumper helps theme creators collect the icons and bundle identifiers currently installed on their device.

### What it does

- Detects app icons visible on the Home Screen
- Exports icon artwork for theme creation
- Records app bundle identifiers
- Creates a ready-to-review dump folder
- Helps match animated assets to the correct installed apps

### How to use it

1. Install **LivingIcons Dumper**.
2. Respring.
3. Swipe through every Home Screen page and folder containing apps.
4. Check the generated dump folder.
5. Use the exported files to build or update a LivingIcons theme.
6. Uninstall the dumper when finished.

LivingIcons Dumper is intended as a temporary theme-development utility, not a tweak that needs to remain installed permanently.

---

## DockPages

DockPages adds swipeable pages to the iPhone dock.

Instead of being limited to one row of dock icons, users can move between multiple dock pages with natural horizontal swipes.

### Features

- Multiple dock pages
- Smooth left and right swiping
- Up to five pages
- Up to four apps per page
- Native-looking page behavior
- Designed for iOS 17
- Relaxin RootHide support
- Automatic `oldabi` dependency installation when required

### Basic use

1. Install **DockPages**.
2. Respring.
3. Add apps to the dock.
4. Swipe horizontally across the dock to move between pages.

DockPages is currently distributed as an alpha build, so users should report their device model, iOS version, Relaxin version, and any SpringBoard issues when submitting feedback.

---

## Repository Packages

| Package | Version | Description |
|---|---:|---|
| LivingIcons | 0.5.7 | Animated Home Screen icons, themes, previews, and per-app controls |
| LivingIcons Dumper | 1.0.0 | Exports app icons and bundle identifiers for theme creation |
| DockPages | 0.4.0-alpha | Adds swipeable pages to the iPhone dock |

---

## Compatibility

Current target environment:

- iOS 17
- Relaxin RootHide
- `iphoneos-arm64e`
- Legacy arm64e Support (`oldabi`)

The `oldabi` package is listed as a dependency for locally built legacy-arm64e tweaks so Sileo installs it automatically from the RootHide repository.

---

## Add the Repository

Use this source URL:

```text
https://dldkdkd.github.io/LivingIcons/
```

Direct Sileo link:

```text
sileo://source/https://dldkdkd.github.io/LivingIcons/
```

---

## Support

When reporting a problem, include:

- Device model
- iOS version
- Relaxin version
- ElleKit version
- LivingIcons or DockPages version
- Active theme
- Whether `oldabi` is installed
- Relevant screenshots or SpringBoard crash logs

---

## Donations

LivingIcons is free.

A PayPal donation button is available inside:

```text
Settings → LivingIcons
```

Donations help support future compatibility updates, new features, and additional animated themes.

---

## Repository Maintenance

This repository is hosted entirely with GitHub Pages.

Static repo files:

- `Release`
- `Packages`
- `Packages.gz`
- `Packages.bz2`
- `debs/`
- `depictions/`
- `assets/`

After replacing or adding a `.deb`, regenerate package metadata with:

```bash
python3 update_repo.py
```

Then commit the updated files to the `main` branch.
