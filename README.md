# Subsync


## Installation
* Clone the repository
* Create a virtual environment `virtualenv venv`
* Install dependencies `pip install -r requirements.txt`

## Getting Started
  * Firstly, add some training material to `/training` folder
    * Movie material and matching subtitle (e.g. *test1.mkv* and *movie1.srt*)
  * Train the neural network `make train`
  * Evaluate the performance of the neural network `make inspect`
