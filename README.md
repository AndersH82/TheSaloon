![The Saloon](readme_media/headerreadme.png)


# The Saloon

Welcome to The Saloon

## Features 

You can register a user on this page. Upon logging in, you will be directed to the start page, where you can read and write Shouts. After writing a Shout, you can visit your profile to view only your Shouts. Additionally, you have the option to upload images to a gallery for all users to see. Navigation is facilitated by the navigation bar located at the top of the page

### Existing Features

- __Navigation Bar__

    - The full responsive navigation bar is available on all pages.
    Upon entering the page, users can press the logo,
    "The Saloon," which then directs them to the start page.
    On the start page, there is a profile list visible only to logged-in users. Additionally, there are registration and login buttons for users who are not yet logged in.

    - Once logged in, users gain access to additional navigation options, including 
    buttons for the profile list, profile, gallery, and log-out. The navigation bar also features a profile picture on the right side, which links to the user's profile. This design is consistent across all pages to facilitate easy navigation, regardless of the device being used.

    - This approach ensures that users can smoothly navigate from page to page
    without needing to rely on the browser's back button, enhancing the overall user experience across all devices.


Here you can see the navigation bar when you log in or register.
![Nav Bar](readme_media/navbarout.png)
    

Here you can see the navigation bar when you are logged in.
![Nav Bar](readme_media/navbarin.png)


- Under the navigation bar, a text appears when you:

- Login

![Login](readme_media/navlogedin.png)

- Logout

![Logout](readme_media/navlogedout.png)

- Register

![Register](readme_media/navregister.png)

- Posted shout

![Shout](readme_media/navshout.png)

- Edit shout

![Edit shout](readme_media/naveditshout.png)

- Update profile

![Update](readme_media/navupdate.png)
- __The landing page image__

    - Here you can see what has been written before you log in or register.

![Landing Page](readme_media/landingimg.png)

 
- __Registration page__

  - Here you can enter username, first name, last name, e-mail, password and 
   then confirm with the same password.

![Register](readme_media/register.png)

- __Login page__

  - Here is the login page where you enter your username and password to enter the 
  website.

![Login](readme_media/login.png)

- __Profile page__

  - On your profile page, you can see your profile bio, which includes a profile picture where you can write a brief bio about yourself. You can also add links to your social media, view your followers and the profiles you follow, and use the follow/unfollow button. Additionally, there's an edit profile button.

![Profile](readme_media/profile.png)

- __Gallery__

  - This page allows the user to upload images for all to see 

![Gallery](readme_media/gallery.png)

- __Profile list__

  - This page shows which users are registered on the page with profile picture and last updated. 

![profil list](readme_media/profilelist.png)

- __Other pages__

  - Then there is the edit page that you access via profile.

  - A page where you get to edit Shouts via the profile if you press edit.


### Some other features ideas for the page

- The user should be able to like or dislike profiles.
- The user must be able to have their own galleries for their images.
- The user could write messages to other users.
## Wireframe

- Here is a framework of what the page would look like when I started planning for this website.

Home page          |  Gallery page
:-------------------------:|:-------------------------:
![Home](readme_media/homeframe.png)  |  ![Gallery](readme_media/galleryframe.png)

Profile page          |  Profile list page
:-------------------------:|:-------------------------:
![Profile](readme_media/profileframe.png)  |  ![Gallery](readme_media/profilelistframe.png)

Login page          |  Registration page
:-------------------------:|:-------------------------:
![Profile](readme_media/loginframe.png)  |  ![Register](readme_media/registerframe.png)





<p align="center"> - Mobile frame -</p>
<p align="center">
  <img src="readme_media/mobileframe.png" width=200 height=400 alt="Description of image">
</p>






## Testing 

### Validator Testing 

- HTML
  - __W3C Validation__

https://validator.w3.org/nu/?doc=https%3A%2F%2Fthesaloon-08255dd425ce.herokuapp.com%2F

    - The page receives 51 Info notes because it contains linebreaks in the html code. 
- CSS
  - __W3C Validation__

 https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthesaloon-08255dd425ce.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv

    - It passed the test but received 707 warnings that the website contains Bootstrap.
### Lighthouse Testing

Update profile page          |  Gallery page
:-------------------------:|:-------------------------:
![Update](readme_media/lighthouseedit.png)  |  ![Gallery](readme_media/lighthousegallery.png)

Home page          |  Login page
:-------------------------:|:-------------------------:
![Home](readme_media/lighthousehome.png)  |  ![Login](readme_media/lighthouselogin.png)

Profile page          |  Profile list page
:-------------------------:|:-------------------------:
![Profile](readme_media/lighthouseprofile.png)  |  ![Login](readme_media/lighthouseprofilelist.png)

Registration page          |  Edit shout page
:-------------------------:|:-------------------------:
![Register](readme_media/lighthouseregister.png)  |  ![Shout](readme_media/lighthouseshout.png)


### Unfixed Bugs

- Found the error at the last second before submitting the project 
    - You must fill in the entire form and add a picture, otherwise you will not progress.
    - Link label, text when uploading image and the button are not styled with css.

## Color Scheme

The base colors          |  Color for social media
:-------------------------:|:-------------------------:
![Color](readme_media/headcolor.png)  |  ![Color](readme_media/linkscolor.png)

## Deployment

- The site was deployed to Heroku.

    - Select the Website to Deploy: On the Heroku home page, choose the website you wish to deploy.
    - Go to the Link: Navigate to the provided link for the website you selected.
    - Find the Push Button: At the top of the page, locate the push button.
    - Choose the Branch: Decide which branch of your repository you want to deploy from.
    - Press the Deploy Button: Finally, click the deploy button at the bottom of the page to initiate the deployment process.

 This process allows you to deploy your website to Heroku directly from the website's home page, making it easy to manage and deploy your projects without needing to use the command line or Heroku CLI.

 Link : https://thesaloon-08255dd425ce.herokuapp.com/

- The site was deployed to GitHub.

  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

Link : https://andersh82.github.io/thesaloon/

- Here you can find the repository:

Link : https://github.com/AndersH82/thesaloon

## Credits 

 - Default image - flaticon.com
 - Code search - Phind
 - Toutorials - youtube
 - Codemy on youtube - The basis of the page
 - Bootstrap
 - W3 school
 - Google
 - Brandcolorcode - links
 - Fontawesome
 - Google fonts
 - My mentor on CI - Rory
 - Coolors.co for colors to the page


## Other Notes

- Argil: I am a beginner at argil, and this is my first time. I'm looking forward to becoming better at argil in the future.

- Readme: I'm pretty happy with my README, but I'm confident that I can improve my work with future assignments.
