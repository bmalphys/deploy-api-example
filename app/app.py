from fastapi import FastAPI, File, UploadFile, HTTPException
        
app = FastAPI()

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        with open(file.filename, 'wb') as f:
            while contents := file.file.read(10* 1024 * 1024):
                f.write(contents)
    except Exception:
        raise HTTPException(status_code = 500, detail = 'Something went wrong')
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}

@app.get('/serverstatus')
async def serverstatus():
    return "ACTIVE"