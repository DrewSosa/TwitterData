import matplotlib
import seaborn
import requests



print("Hello World!")
key = "edQcYUUZAsIcwRRkrE8WlnG7p"
secretKey = "ZptJukk6B0hnsXlfD18cwLauO5B6M0252rqvn4ajrs7BJ6HGUT"
# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

data = r.json()

curl --request POST \
  --url https://api.twitter.com/1.1/tweets/search/30day/knowhow.json \
  --header 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAAFql9wAAAAAANAjG9fLYn%2BzhSz88yFA9XhT7qW0%3DfZa2S7eGag5zQNJuNXHk8ORq3LU7IrL3Ec54oGroFvzhYxOZRm' \
  --header 'content-type: application/json' \
  --data '{
                "query":"from:TwitterDev lang:en",
                "maxResults": "100",
                "fromDate":"202006210000",
                "toDate":"202007010000"
                }'

curl --request POST \
  --url https://api.twitter.com/1.1/tweets/search/30day/knowhow/counts.json \
  --header 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAAFql9wAAAAAANAjG9fLYn%2BzhSz88yFA9XhT7qW0%3DfZa2S7eGag5zQNJuNXHk8ORq3LU7IrL3Ec54oGroFvzhYxOZRm' \
  --header 'content-type: application/json' \
  --data '{
                "query":"from:TwitterDev lang:en",
                "fromDate":"202006210000",
                "toDate":"202006210000",
                "bucket": "day"
                }'

curl -u 'edQcYUUZAsIcwRRkrE8WlnG7p:ZptJukk6B0hnsXlfD18cwLauO5B6M0252rqvn4ajrs7BJ6HGUT' \
  --data 'grant_type=client_credentials' \
  'https://api.twitter.com/oauth2/token'

bearerToken = 'AAAAAAAAAAAAAAAAAAAAAFql9wAAAAAANAjG9fLYn%2BzhSz88yFA9XhT7qW0%3DfZa2S7eGag5zQNJuNXHk8ORq3LU7IrL3Ec54oGroFvzhYxOZRm'


