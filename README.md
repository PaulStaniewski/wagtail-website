# Wagtail Website

This project is a website built using the '[Creative Bootstrap theme](https://startbootstrap.com/theme/creative)' and the '[Wagtail CMS](https://wagtail.io/)'.
The website is divided into several sections, each of which can be easily edited from the Wagtail admin panel. Added two more Pages (Gallery and Attractions Page)



# Features
   
   - Banner section: You can change the title, subtitle and banner image from the admin panel.
   ![baner-section-website](https://user-images.githubusercontent.com/31824304/213744305-6e9c80c8-6ac6-4c27-9ff7-b65367169c48.JPG)   
   - Carousel section: You can change the title, subtitle and images for the carousel from the admin panel.
   ![carousel-section-website](https://user-images.githubusercontent.com/31824304/213744435-25c8f8dd-a1f5-4f83-a645-3c4fd0f02906.JPG)   
   - Attractions section: You can add your own photos, titles and captions for the attractions from the admin panel (in theme that was portfolio section).
   ![attractions-section-website](https://user-images.githubusercontent.com/31824304/213744465-14b7c75f-2367-4ae9-92fc-e8c8cd59ac22.JPG)   
   - Footer section: You can change the company name and year of creation of the website.
   ![footer-section-website](https://user-images.githubusercontent.com/31824304/213746049-ebf45845-0cae-4e6e-aac5-4db52e902108.JPG)   
   - Gallery Page: You can change the content and upload your own images using the admin panel. 
     The gallery is built using the '[Bootstrap Album example](https://getbootstrap.com/docs/4.0/examples/album/)', and it's using '[SimpleLightbox](https://simplelightbox.com/)'
     to preview added pictures.
   ![gallery_page_website](https://user-images.githubusercontent.com/31824304/213746108-796012c9-639f-4120-94bd-9b0976ee278c.JPG)   
   - Attraction page: Still under construction. Trying to make it more flexible.   
   ![attractions-another-page](https://user-images.githubusercontent.com/31824304/213753110-918d351d-e0d2-4fbe-a87c-08272547cdb0.JPG)

   
# Admin Panel
- Banner section
![wagtail_home_banner](https://user-images.githubusercontent.com/31824304/213751388-a735366f-424e-42a8-bc87-d3a2b1dfd3f9.JPG)
- Carousel section
![carousel](https://user-images.githubusercontent.com/31824304/213752405-ebcbed01-b00b-49e8-93b4-2bb1406851f3.JPG)
- Attractions section
![attractions-admin](https://user-images.githubusercontent.com/31824304/213752721-561d4690-7455-42a2-8b92-253144a026df.JPG)
- Footer section
![footer-admin](https://user-images.githubusercontent.com/31824304/213752901-0156af21-5b3d-4cbf-a7c4-d77a507a8066.JPG)

# Installation

    1.Download the project and unpack it.
    2.Open it in Visual Studio Code or other code editor.
    3.Open the terminal and navigate to the folder where the manage.py file is located.
    4.Run the command .\Scripts\activate to activate the virtual environment.
    5.In the blogsite/settings/dev.py file, change the SECRET_KEY value from SECRET_KEY = config("SECRET_KEY") to SECRET_KEY = "#YOUR KEY"
    6.Run the command py .\manage.py createsuperuser to create a superuser account.
    7.Run the command py .\manage.py runserver to start the development server and access the application on http://127.0.0.1:8000/

Please note that you may need to install the necessary dependencies before running the application. You can do this by running the command pip install -r requirements.txt in the terminal.

Also, it's necessary to have installed Python and Django in your machine to be able to run the application.

Now you can access the application and customize it through the admin panel (http://127.0.0.1:8000/admin/) using the superuser credentials that you created.



# Future plans

   - Styling for the attractions page.
   - Use the wagtail-icon-picker module to change the bootstrap icons from the Wagtail admin panel.
   - Change some logic in the gallery page.
   

# Conclusion

Overall, this project is a great example of how the Wagtail CMS can be used to create a fully customizable website.
With its easy-to-use admin panel, you can easily change the content and design of your website without any technical knowledge.
The project is not finished yet, but it have a lot of potentials, and you can use it as a starting point for your own project.
