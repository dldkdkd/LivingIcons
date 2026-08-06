# LivingIcons GitHub Pages Repo

This folder is ready for the GitHub repository:

- GitHub username: `dldkdkd`
- Repository: `LivingIcons`
- Sileo source: `https://dldkdkd.github.io/LivingIcons/`

## Upload with the GitHub website

1. Open your new `LivingIcons` repository.
2. Click **Add file → Upload files**.
3. Extract `LivingIcons_GitHub_Pages_Repo.zip` on your PC.
4. Drag **all files and folders inside the extracted folder** into GitHub.
   Do not upload the outer folder as one nested folder.
5. Commit directly to `main`.

## Enable GitHub Pages

1. Open **Settings → Pages** in the repository.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Branch: `main`
4. Folder: `/ (root)`
5. Save.

Your source will be:

`https://dldkdkd.github.io/LivingIcons/`

## Test

Open these in a browser:

- `https://dldkdkd.github.io/LivingIcons/`
- `https://dldkdkd.github.io/LivingIcons/Release`
- `https://dldkdkd.github.io/LivingIcons/Packages`
- `https://dldkdkd.github.io/LivingIcons/Packages.gz`

Then add `https://dldkdkd.github.io/LivingIcons/` to Sileo and refresh sources.

## Updating a package

1. Replace the `.deb` in `debs/`.
2. Regenerate `Packages`, `Packages.gz`, and `Packages.bz2`.
3. Commit the changed files.

The current static repo includes LivingIcons, LivingIcons Dumper, and DockPages.
