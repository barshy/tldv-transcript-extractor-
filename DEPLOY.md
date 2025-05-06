# Deploying to Netlify

You can easily deploy this project to Netlify using Netlify Drop. Here's how:

## Method 1: Netlify Drop (Easiest)

1. Go to [Netlify Drop](https://app.netlify.com/drop)
2. Drag and drop the entire project folder onto the Netlify Drop zone
3. Wait for the upload and deployment to complete
4. Your site will be live at a random subdomain like `random-name.netlify.app`
5. You can customize this subdomain in the Netlify dashboard

## Method 2: GitHub Integration

If you prefer to use GitHub:

1. Create a new GitHub repository
2. Push your code to the repository:
   ```
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git branch -M main
   git push -u origin main
   ```
3. Log in to [Netlify](https://app.netlify.com/)
4. Click "New site from Git"
5. Select GitHub and authorize Netlify
6. Select your repository
7. Configure build settings (leave defaults for this project)
8. Click "Deploy site"

## Customizing Your Domain

After deployment:

1. Go to your site settings in Netlify
2. Click on "Domain settings"
3. You can:
   - Customize your Netlify subdomain
   - Add a custom domain you own
   - Purchase a domain through Netlify

## Updating Your Site

To update your site:

- If using Netlify Drop: Simply drag and drop the folder again
- If using GitHub: Push changes to your repository, and Netlify will automatically redeploy
