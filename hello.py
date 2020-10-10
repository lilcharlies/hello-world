import tweepy

auth = tweepy.OAuthHandler("AM48CG88cNoGUVAeX62NXv9Fx", "zsw3lDnFLcJsVmfTkaylnUB5dcqJKCgzheonaIWVO3Nkrgp1FJ")
auth.set_access_token("1832298932-LABp8frmHUTd4Cztxyrs0wprk4ZpteTY0A3IMLa", "KyOjlSahbtM2LHRWuBSRLnZ5CDLaUo7ylZOZ6CeK5jvlF")

api = tweepy.API(auth)

api.update_status("hi")
