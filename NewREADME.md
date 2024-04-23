# Social Media Platform

## Overview

This project is a Django-based social media platform where users can create profiles, post shouts, upload images, and interact with each other. It includes features like user registration, profile management, shouting, and image uploading.

## Features

- User Registration: Allows new users to sign up.
- Profile Management: Users can create and update their profiles, including profile pictures and social links.
- Shouting: Users can post shouts that can be liked by others.
- Image Uploading: Users can upload images to share with their followers.
- Interaction: Users can follow others, like shouts, and delete their own shouts and images.

## User Stories

- As a new user, I want to sign up for an account so that I can start using the platform.
- As a user, I want to create and update my profile so that I can share my information with others.
- As a user, I want to post shouts so that I can share my thoughts and ideas.
- As a user, I want to like shouts so that I can show my support.
- As a user, I want to upload images so that I can share my moments with others.
- As a user, I want to follow others so that I can see their shouts and images in my feed.

## UX Design

The user interface is designed to be simple and intuitive. Users can easily navigate through the platform to create profiles, post shouts, upload images, and interact with others. The design is responsive, ensuring a good user experience on both desktop and mobile devices.

## Flowchart

Start 
  | 
  V 
User Registration
  | 
  V 
User Login 
  | 
  V 
Home Page (Shout Feed) 
  | 
  V 
Profile Management 
  | 
  V 
Shouting 
  | 
  V 
Image Uploading 
  | 
  V 
Interaction (Follow, Like, Comment) 
  | 
  V 
 End


## Setup

### Prerequisites

- Python 3.x
- Django 3.x
- PostgreSQL (or any other supported database)

### Installation

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd <project_directory>`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up the database: `python manage.py migrate`
5. Run the server: `python manage.py runserver`

## Usage

After setting up, you can access the platform by navigating to `http://localhost:8000` in your web browser. From there, you can sign up, log in, and start using the platform.

## Contributing

Contributions are welcome. Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
