import uvicorn 



if __name__ ==  "__main__": 
    uvicorn.run("app.app:app" , host = "0.0.0.0" , port = 8000 , reload = True )

    # * it can be app.app:hi if there is name of our api is hi 
    # * host is defining the domain we can access it localhost 
    