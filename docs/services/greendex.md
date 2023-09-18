# GREENDEX service

<img src="https://raw.githubusercontent.com/red5ai/estaty/main/docs/media/greendex_logo.png" width="600"/>

**"Greendex"**: 

1. Service with API which can calculate simple Environmental, Social, and Governance (ESG) parameter 
    for real estate assets using addresses: Swagger UI [https://api.greendex.wiredhut.com/docs](https://api.greendex.wiredhut.com/docs)
2. A Google spreadsheet add on which can be executed as Excel function like `SUM` (or any other familiar function) which can calculate simple characteristic how "green" the building's surrounding is. 

<img src="https://raw.githubusercontent.com/red5ai/estaty/main/docs/media/greendex_example.png" width="650"/>

The service allows users to estimate the “greenness” of a building's (asset’s) location. For this purpose, the area of green spaces is calculated using open sources of cartographic data. The ratio of this “green” area to the total area within the geometry is then calculated. Green space includes parks, flowerbeds, etc. 
The size of the area to be analyzed is determined by the radius (in meters). 

## Spreadsheet usage example

Use function `=GREENDEX(P1, P2)` with two parameters:

- `P1`. First parameter, address as text. Example: `Berlin, Neustädtische Kirchstraße 4-7`
- `P2`. Second parameter, radius for area in meters. Example: `500`

## How to understand is the obtained green value good or not 

As is clear from the description of the indicator, it can vary from 0 to 100. 
But to understand how good a number is obtained for the selected asset, it is better to have statistics on several launches. 

For example, using the greendex service the benchmark for Berlin was prepared: 

<img src="https://raw.githubusercontent.com/red5ai/estaty/main/docs/media/greendex_berlin_benchmark_map.png" width="650"/>

On the map is shown green index evaluation for randomly chosen points in administrative boundaries of Berlin in buildings extent. 

Histogram of green index values for Berlin: 

<img src="https://raw.githubusercontent.com/red5ai/estaty/main/docs/media/greendex_berlin_benchmark_scale.png" width="650"/>

In this way, the obtained value can be compared with other buildings in Berlin and it is possible to figure out whether it is "greener" than other objects.

## Privacy policy

*Last update: September 18, 2023*

This Privacy Policy describes how **greendex** collects, uses and exposes information, and the choices that you have with respect to that information.
The Service hereinafter is the [https://api.greendex.wiredhut.com/docs](https://api.greendex.wiredhut.com/docs) website, application, Google Sheets add-on.

We use your Personal Information only for providing and improving the service. 
By using the service, you agree to the collection and use of information in accordance with this policy.

### Information Collection And Use

While using our service, we may ask you to provide us with certain personally identifiable 
information that can be used to contact or identify you. 
Personally identifiable information may include, but is not limited to your name ("Personal Information").

### Log Data

Like many services operators, we collect information that your browser (or third party 
services you use to utilize **greendex** service capabilities) 
sends whenever you use our service ("Log Data").

The information is collected completely anonymously and is only used for the purpose of improving the service. Examples of data used: number of requests to the service.

### Cookies

Cookies are files with small amount of data, 
which may include an anonymous unique identifier. Cookies are sent to your browser from a web site and stored on your computer's hard drive.

Like many sites, we use "cookies" to collect information. 
You can instruct your browser to refuse all cookies or to indicate when a cookie is being sent. 
However, if you do not accept cookies, you may not be able to use some portions of our Site.

### Security

The security of your Personal Information is important to us, but remember that no method of transmission over the 
Internet, or method of electronic storage, is 100% secure. While we strive to use commercially acceptable means to protect your 
Personal Information, we cannot guarantee its absolute security.

### Changes To This Privacy Policy

This Privacy Policy is effective as of (add date) and will remain in effect except with 
respect to any changes in its provisions in the future, which will be in effect immediately after being posted on this page.

We reserve the right to update or change our Privacy Policy at any time and you 
should check this Privacy Policy periodically. Your continued use of the Service after 
we post any modifications to the Privacy Policy on this page will constitute your acknowledgment of 
the modifications and your consent to abide and be bound by the modified Privacy Policy.

If we make any material changes to this Privacy Policy, we will notify you either through the email address you have provided us, 
or by placing a prominent notice on [our website](https://wiredhut.com/).

### Contact Us

If you have any questions about this Privacy Policy, please contact us.


## Terms of service

*Last update: September 18, 2023*

## Contacts 

If you want to ask questions to the developers personally or learn about custom development, 
then feel free to visit the official website of the company that develops this product: [Wiredhut](https://wiredhut.com/)