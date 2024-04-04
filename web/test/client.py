import requests

if __name__ == '__main__':
    # perform a POST request to the server using the add endpoint with the json parameter
    r = requests.post('http://localhost/predict', 
                      json=[
    0.7570133,
    0.52519528,
    0.56393208,
    0.55820649,
    0.06329663,
    0.50592782,
    1.0,
    1.0,
    0.0,
    0.0,
    1.0,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0,
    0.0,
    0.0,
    1.0,
    0.0,
    0.85869849,
    0.0,
    1.0,
    1.0,
    1.0
])
    # display the request status
    print('Status code: {}'.format(r.status_code))
    # implement result processing
    if r.status_code == 200:
        # if the request was completed successfully (processing code=200),
        # display the result on the screen
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # if the request is completed with a code other than 200,
        # display the contents of the response
        print(r.text)