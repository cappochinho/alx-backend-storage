-- Lists all bands with Glam rock as main style

SELECT band_name, (IFNULL(split, 2020) - formed)
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
