-- Lists all bands with Glam rock as main style

SELECT band_name, DIFFERENCE(split, formed) AS lifespan
FROM metal_bands
WHERE style='Glam rock'
GROUP BY band_name
ORDER BY lifespan DESC;
