-- Lists all bands with Glam rock as main style

SELECT band_name,
       (YEAR(COALESCE(split, NOW())) - YEAR(COALESCE(formed, NOW()))) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
