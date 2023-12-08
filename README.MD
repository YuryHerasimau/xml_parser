# TrainingData.Solutions Interview Task #2
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Test task for the position of technical support trainee with knowledge of Python at [TrainingData](https://trainingdata.notion.site/TrainingData-Solutions-716057e76ab64e0988c39f381a8987ec)


## Description
`2. Marking task`

Attached are 3 xml files: [annotations.xml](https://file.notion.so/f/f/ed3ae53a-9b03-4086-aefc-af27269b6a08/2f4c7804-28c5-4530-8792-1f677d0e381f/annotations.xml?id=3dd5aa28-b525-42e9-896e-8f98bc222050&table=block&spaceId=ed3ae53a-9b03-4086-aefc-af27269b6a08&expirationTimestamp=1702159200000&signature=0byQRh8SMYeXbDlIXKca6KucAVLm1J41EVGzdTSL9pE&downloadName=annotations.xml), [annotations-2.xml](https://file.notion.so/f/f/ed3ae53a-9b03-4086-aefc-af27269b6a08/8d34b0d8-d89f-4faf-b5eb-a6255b4e629e/annotations-2.xml?id=d3aab611-084a-423e-988d-148460bed756&table=block&spaceId=ed3ae53a-9b03-4086-aefc-af27269b6a08&expirationTimestamp=1702159200000&signature=R8ahDOlt8um6UKJ2PWfiWTv-7F8a890VC_xHRisjy_8&downloadName=annotations-2.xml), [annotations-3.xml](https://file.notion.so/f/f/ed3ae53a-9b03-4086-aefc-af27269b6a08/3606e8ad-8da1-48e9-9d25-47463c4ce38f/annotations-3.xml?id=37583342-0187-4246-bdbf-164262129678&table=block&spaceId=ed3ae53a-9b03-4086-aefc-af27269b6a08&expirationTimestamp=1702159200000&signature=qd4ZDYs7lMlUehlKzzAfdl5QSpJ57JlfX_w8qfcX1m0&downloadName=annotations-3.xml).
Your task is to get the quantity:

1. Total images
2. Total images marked
3. (if any) Unlabeled images
4. Statistics by class:

For example:
> class 1: 100 figures (boxing, polygon, etc. - all together)
> class 2: 200 figures (boxing, polygon, etc. - all together)

5. Number of digits (total)
5*. Statistics on figures:

For example:
> polygons: 4444 pcs.
> boxes: 1000 pcs.

6. Name and parameters (width, height) of the largest image and the smallest. If there are several, display the number such images and display the information of any one image.
7. Change the IDs of the images - make them in reverse order.
8. Change the name of the image - change the extension to “png”.
9. Change the name of the image - remove the path to the file, leave only the name of the file itself.

Write 4 scripts, the script should work for all markups:
- 1 script: 1, 2, 3, 5, 6 - general statistics
- 2 script: 4 - Statistics by class
- 3 script: 5* - Statistics on figures
- 4 script: 7, 8, 9 - changing the xml file

Explanations:
> figures: box, polygon, point
> class: ignore, fur, item

## Getting Started

### Installing
1. Clone the repository:
```
git clone <repo>
```

### Executing program
Run the script:
```
python total_stats.py
python stats_by_class.py
python stats_by_figure.py
python update_xml.py
```