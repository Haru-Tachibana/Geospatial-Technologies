# Lecture 7: Capturing 3D Models

## 7.1 Radar & LiDAR

### most terrain data are captured from air

### differentce: Radar is higher, LiDAR has higher resolution (Radar: 5m, LiDAR: 2m)

### DTM (Digital Terrain Models), DSM (Digital Surface Models), TIN (Triangular Irregular Models)

- TIN is really effienent (game engines use this a lot), reduced data abundance, can render rq
- less common in GIS sys. for most data are in grid forms

### LiDAR

- stripping algorithm
- ![](https://www.theotop.ro/custom_images/pagini/servicii/img_4_foto_dtm_vs_dsm.jpg)
- ![](https://isprs-annals.copernicus.org/articles/II-3-W4/157/2015/isprsannals-II-3-W4-157-2015.html)

### VGE - Virtual Geographic Env.
- typical workflow: DSM -> Stripped DTM -> true 3D models added
  

## 7.2 - Photogrammic Techniques and Drones

### Complex workflow to create ture 3D buidings

### Stereo

### auto-texturing

- add jpg textures to 3D polygons

### Google Earth

- continous photo mesh rather than add photos to each building to increrase the consistence of buildings
- cloud-sourcing in early stages
  
### MetroVista - bluesky
- UK company, similar to Google Earth
- they didn't publish the source code for algorithom
- 1st hybrid airbone approach (?)
- ==see prctical session for more info (week 7)==
  
### Structure from Motion
- capuring multiple views whilist moving around an object
- software can automatically recognise features and construct 3D models (e.g., software name: VisualSFM, CouldComapre)
- some software like CloudCompare can handle with missing facets
- view more: [link to sketchfab](https://sketchfab.com/)
