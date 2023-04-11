# AI- IMAGER

## Server-side

### Features

1. Generate image based on description

```py
response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
```

2. Create edits - masking images [2]

```py
response = openai.Image.create_edit(
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
```

3. Generate variation

```py
response = openai.Image.create_variation(
  image=open("corgi_and_cat_paw.png", "rb"),
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
```

#### Upload Conditions

- Less than 4MB
- A square PNG Image

## Server side

### Features

- Takes in OPENAI-API-KEY as login credentials
- Fills in a form - (Editing mode,Prompt,Image)
- Return list of urls then display them.