# Tone Analyzer Microservice

View on [Heroku!](https://tone-analyzer-microservice.herokuapp.com/)

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Build Status](https://travis-ci.com/travis-ci/travis-web.svg?branch=master)](https://travis-ci.com/github/Vivid-Project/microservice)


  <h3 align="center">Tone Analyzer Microservice</h3>

  <p align="center">
    This is a microservice that was built to provide a tone analysis for a user's dream journal entry.
    <br />
    <a href="https://github.com/Vivid-Project/microservice"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- for adding a demo video
    <a href="Add our video link here">View Demo</a>  · -->
    ·
    <a href="https://https://github.com/Vivid-Project/microservice/issues">Report Bug</a>
    ·
    <a href="https://https://github.com/Vivid-Project/microservice/issues">Request Feature</a>
  </p>
</p></br>




<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Configuration](#configuration)
  * [Testing](#testing)
  * [Endpoints](#endpoints)
* [Contributing](#contributing)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

</br></br>


<!-- ABOUT THE PROJECT -->
## About The Project
Please visit the [frontend](https://github.com/Vivid-Project/frontend) repository of this project and check out the readme there for a more in depth look at this project!

This microservice was built to provide tone analysis data for a user's dream journal entry. This microservice works in tandem with the [Vivid-Project backend](https://github.com/Vivid-Project/backend). When a user saves a dream journal entry it is sent to the Vivid-Project backend where that entry is stored in the database. From there, a request will be issued to this microservice containing a raw text body holding that journal entry. This microservice will analyze this text, sentence by sentence, and will return a "tone strength"(a count of how many times a given tone was present in the analysis), as well as "unique tones"(a string containing each unique tone name for this request).  Please visit the usage section of this document for more information on what that request / response looks like.


This micro services uses the IBM Tone Analyzer API.  Read the API documentation [here](https://cloud.ibm.com/apidocs/tone-analyzer?code=python)

To view all the repositories associated with Vivid, please visit [Vivid-Project](https://github.com/Vivid-Project)
</br>

### Built With


* [Python](https://github.com/python)
* [Flask](https://github.com/pallets/flask)
</br>

<!-- GETTING STARTED -->
## Getting Started

To properly use this application you will need to set up and configure three repositories. Follow the *Configuration* directions in each repository to get Vivd running locally! Alternatively, check out the production application [here](put front end heroku here)!!!
</br>

### Prerequisites
These setup instructions are for Mac OS.

#### Install Necessary Programs
Be sure your machine has `Python` installed.
[Postman](https://www.postman.com/) is required for sending requests and verifying API responses from the IBM Watson Tone Analyzer API.
</br>

### Configuration
**Setting Up this Microservice**
1. Clone this repo ```git clone git@github.com:Vivid-Project/microservice.git```

2. Enter the directory it was cloned into ```cd microservice```

3. Run `pip install -r requirements.txt` to install dependencies

4. Go [here](https://cloud.ibm.com/apidocs/tone-analyzer?code=python) and sign up for a free api key

5. Run `touch .env` and in this file add your api key in this format: ```TONE_ANALYZER_API_KEY = 'your-key-here'```
</br>


### Endpoints
#### Quick Start
This microservice has a single end point. To quickly use this endpoint please direct requests to https://tone-analyzer-microservice.herokuapp.com/microservice/api/v1.0/tones (our deployed application).

It only needs to be given a raw text body in the request to generate a response. Punctuation is important, as this service will analyze the given input sentence by sentence. Alternatively, ensure each new sentence starts on a new line.

It should be noted that for this microservice to run optimally, it currently only accepts English or French. It is recommended that you use one or the other and not both if wanting to achieve the highest accuracy from the tone analyzer api. </br>


This collection has been set up for you. One request is set up to run from our deployed heroku application, the other for if you are running locally!

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/9ca6f197c67ca669a7be)</br></br>

**POST /microservice/api/v1.0/tones**
</br></br>


Example raw text # 1:

<details></br>
There is no pain, you are receding.
A distant ship, smoke on the horizon.
You are only coming through in waves.
Your lips move, but I can't hear what you're saying.
When I was a child, I had a fever.
My hands felt just like two balloons.
Now I've got that feeling once again.
I can't explain, you would not understand.
This is not how I am.
</details></br></br></br>


Example raw text # 2(No Punctuation):

<details></br>
There is no pain, you are receding</br>
A distant ship, smoke on the horizon</br>
You are only coming through in waves</br>
Your lips move, but I can't hear what you're saying</br>
When I was a child, I had a fever</br>
My hands felt just like two balloons</br>
Now I've got that feeling once again</br>
I can't explain, you would not understand</br>
This is not how I am
</details></br></br></br>

Example Response:

<details>

```ruby
{
    "tone_strength": {
        "Analytical": 2,
        "Joy": 1,
        "Tentative": 1
    },
    "unique_tones": "Analytical, Joy, Tentative"
}
```
</details></br>


##### For local use
After completing the configuration steps,  

1. In the command line run ```python run.py```  This will spin up your local server.

2. Open up Postman and using a ```POST``` to localhost ``` http://127.0.0.1:5000/microservice/api/v1.0/tones```, include a raw text body and you are ready to go!
</br>


### Testing

[Pytest](https://github.com/pytest-dev/pytest) was used for the testing of this microservice.

To view the test coverage;

Once inside your terminal within the microservice directory run the following command.

```
coverage report
```
This will show you the quick summary of the test coverage in this application.

Alternatively, you can run ```coverage html``` to generate a folder containing a more detailed analysis of the coverage in this repository. Simply navigate to the full path of the file in your browser to view these reports.

</br>

<!-- ROADMAP -->
## Roadmap

See [Open Issues](https://github.com/Vivid-Project/microservice/issues) or visit our [Project Board](https://github.com/orgs/Vivid-Project/projects/1) for a list of proposed features, known issues, and project extensions.

</br>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make this community such an amazing and fun place to learn, grow, and create! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch ```git checkout -b feature/NewGreatFeature```
3. Commit your Changes ```git commit -m 'Add some NewGreatFeature'```
4. Push to the Branch ```git push origin feature/NewGreatFeature```
5. Open a new Pull Request!

</br>
<!-- CONTACT -->
## Contact

Amanda Davidson &nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/amanda-davidson02/) - [GitHub](https://github.com/ADavidson02) - [Turing Alum Profile](https://alumni.turing.io/alumni/amanda-davidson)

Shawn Truesdale &nbsp;&nbsp;&nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/shawntruesdale/) - [GitHub](https://github.com/Shawntru)

Jonathan Wilson &nbsp;&nbsp;&nbsp;&nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jonathan--wilson/) - [GitHub](https://github.com/Jonathan-M-Wilson) - [Turing Alum Profile](https://alumni.turing.io/alumni/jonathan-wilson)

Zach Stearns &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/zach-stearns/) - [GitHub](https://github.com/Stearnzy) - [Turing Alum Profile](https://alumni.turing.io/alumni/zach-stearns)

Aidan Murray &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/aidan-murray-teknoserval/) - [GitHub](https://github.com/TeknoServal)

Taylor Phillips &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/taphill/) - [GitHub](https://github.com/taphill) - [Turing Alum Profile](https://alumni.turing.io/alumni/taylor-phillips)




Project Link: [Vivid](https://github.com/Vivid-Project)


<!-- ACKNOWLEDGEMENTS -->
<!-- Add resources that were used to help create this project here -->


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Vivid-Project/microservice
[contributors-url]: https://github.com/Vivid-Project/microservice/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vivid-Project/microservice
[forks-url]: https://github.com/Vivid-Project/microservice/network/members
[stars-shield]: https://img.shields.io/github/stars/Vivid-Project/microservice
[stars-url]: https://github.com/Vivid-Project/microservice/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vivid-Project/microservice
[issues-url]: https://https://github.com/Vivid-Project/microservice/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
