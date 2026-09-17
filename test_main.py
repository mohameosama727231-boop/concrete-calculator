import pytest
from main import (
    beam_volume,
    column_volume,
    slab_volume,
    footing_volume,
    calculate_materials
)

def test_beam_volume():
    assert beam_volume(2.0, 0.3, 0.5) == 0.3
    with pytest.raises(ValueError):
        beam_volume(-1.0, 2.0, 3.0)
    with pytest.raises(ValueError):
        beam_volume(0, 2.0, 3.0)

def test_column_volume():
    assert column_volume(0.4, 0.4, 3.0) == 0.48
    with pytest.raises(ValueError):
        column_volume(0.4, -1.0, 3.0)

def test_slab_volume():
    assert slab_volume(5.0, 4.0, 0.15) == 3.0
    with pytest.raises(ValueError):
        slab_volume(5.0, 4.0, 0)

def test_footing_volume():
    assert footing_volume(2.0, 2.0, 0.5) == 2.0
    with pytest.raises(ValueError):
        footing_volume(-2.0, 2.0, 0.5)

def test_calculate_materials_logic():
    # Wet volume = 10 m3, M15 ratio 1:2:4 (total = 7)
    # Dry volume = 10 * 1.54 = 15.4 m3
    res = calculate_materials("Beam", 10.0, "M15")
    
    assert res.wet_volume_m3 == 10.0
    assert res.dry_volume_m3 == 15.4
    # Cement m3 = 15.4 * (1/7) = 2.2
    assert res.cement_m3 == 2.2
    # Cement kg = 2.2 * 1440 = 3168.0
    assert res.cement_kg == 3168.0
    # Cement bags = 3168 / 50 = 63.36
    assert res.cement_bags == 63.36

def test_calculate_materials_errors():
    with pytest.raises(ValueError):
        calculate_materials("Beam", 0, "M20")
    with pytest.raises(ValueError):
        calculate_materials("Beam", -5, "M20")
    with pytest.raises(ValueError):
        calculate_materials("Beam", 5, "INVALID")
