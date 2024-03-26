from fastapi import FastAPI, HTTPException, status, UploadFile, File
# from chintus.codebase import process_file, process_output

app = FastAPI()


# Root
@app.get('/')
async def root():
    """ Root function """
    return {"message": "Welcome to Chitros API"}

@app.get("/ping")
async def pong():
    """ Ping Pong """
    return {"ping": "pong!"}

@app.get("/process")
async def process_file(file: UploadFile = File(...), status_code=status.HTTP_200_OK):
    """ Process the file """
    # Save file in media folder
    with open(f"media/{file.filename}", "wb") as buffer:
        buffer.write(await file.file.read())
    
    # Process the file
    # process_output = process_file(f"media/{file.filename}")
    
    result = ""
    # result = process_output(process_output)

    return {"result": ""}


