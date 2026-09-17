"""
Concrete Quantity Calculator
A civil engineering command-line tool to estimate concrete volume 
and raw material quantities (cement, sand, aggregate) for structural elements.
"""

from dataclasses import dataclass

@dataclass
class MaterialResult:
    element: str
    wet_volume_m3: float
    dry_volume_m3: float
    cement_m3: float
    cement_kg: float
    cement_bags: float
    sand_m3: float
    aggregate_m3: float


def get_valid_input(prompt: str) -> float:
    """Prompt user for a positive numeric value, handling invalid inputs gracefully."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be greater than zero.")
            return value
        except ValueError as e:
            if "must be greater than zero" in str(e):
                print("❌ Error: Please enter a number greater than 0.")
            else:
                print("❌ Error: Invalid input. Please enter a valid number.")


def beam_volume(length: float, width: float, depth: float) -> float:
    if length <= 0 or width <= 0 or depth <= 0:
        raise ValueError("Dimensions must be positive.")
    return length * width * depth


def column_volume(width: float, breadth: float, height: float) -> float:
    if width <= 0 or breadth <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive.")
    return width * breadth * height


def slab_volume(length: float, width: float, thickness: float) -> float:
    if length <= 0 or width <= 0 or thickness <= 0:
        raise ValueError("Dimensions must be positive.")
    return length * width * thickness


def footing_volume(length: float, width: float, depth: float) -> float:
    if length <= 0 or width <= 0 or depth <= 0:
        raise ValueError("Dimensions must be positive.")
    return length * width * depth


def calculate_materials(element: str, wet_volume: float, ratio_choice: str) -> MaterialResult:
    if wet_volume <= 0:
        raise ValueError("Wet volume must be greater than zero.")

    # Define mix ratios and total parts
    mix_ratios = {
        "M15": {"cement": 1, "sand": 2, "aggregate": 4, "total": 7},
        "M20": {"cement": 1, "sand": 1.5, "aggregate": 3, "total": 5.5},
        "M25": {"cement": 1, "sand": 1, "aggregate": 2, "total": 4}
    }

    if ratio_choice not in mix_ratios:
        raise ValueError("Invalid mix ratio choice.")

    mix = mix_ratios[ratio_choice]
    
    # Standard dry volume factor accounting for voids
    dry_volume = wet_volume * 1.54

    cement_m3 = dry_volume * (mix["cement"] / mix["total"])
    sand_m3 = dry_volume * (mix["sand"] / mix["total"])
    aggregate_m3 = dry_volume * (mix["aggregate"] / mix["total"])

    cement_kg = cement_m3 * 1440  # Density of cement = 1440 kg/m3
    cement_bags = cement_kg / 50  # Standard bag = 50 kg

    return MaterialResult(
        element=element,
        wet_volume_m3=round(wet_volume, 3),
        dry_volume_m3=round(dry_volume, 3),
        cement_m3=round(cement_m3, 3),
        cement_kg=round(cement_kg, 2),
        cement_bags=round(cement_bags, 2),
        sand_m3=round(sand_m3, 3),
        aggregate_m3=round(aggregate_m3, 3)
    )


def print_report(res: MaterialResult, mix_name: str):
    print("\n" + "="*50)
    print(f"       CONCRETE QUANTITY ESTIMATION REPORT")
    print("="*50)
    print(f" Structural Element : {res.element}")
    print(f" Concrete Mix Grade : {mix_name}")
    print("-" * 50)
    print(f" Wet Volume (Actual) : {res.wet_volume_m3} m³")
    print(f" Dry Volume (1.54)   : {res.dry_volume_m3} m³")
    print("-" * 50)
    print(f" REQUIRED MATERIALS:")
    print(f"   • Cement   : {res.cement_kg} kg (~{res.cement_bags} bags of 50kg)")
    print(f"   • Sand     : {res.sand_m3} m³")
    print(f"   • Aggregate: {res.aggregate_m3} m³")
    print("="*50 + "\n")


def main():
    print("=== Welcome to Concrete Quantity Calculator ===")
    
    while True:
        print("\nSelect Structural Element:")
        print("1. Beam")
        print("2. Column")
        print("3. Slab")
        print("4. Isolated Footing")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '5':
            print("Exiting application. Goodbye!")
            break
            
        element_map = {'1': 'Beam', '2': 'Column', '3': 'Slab', '4': 'Isolated Footing'}
        if choice not in element_map:
            print("❌ Invalid choice. Please select between 1 and 5.")
            continue
            
        element_name = element_map[choice]
        
        print(f"\nEnter dimensions for {element_name}:")
        if choice == '1':
            l = get_valid_input("Enter length (m): ")
            w = get_valid_input("Enter width (m): ")
            d = get_valid_input("Enter depth (m): ")
            vol = beam_volume(l, w, d)
        elif choice == '2':
            w = get_valid_input("Enter width (m): ")
            b = get_valid_input("Enter breadth (m): ")
            h = get_valid_input("Enter height (m): ")
            vol = column_volume(w, b, h)
        elif choice == '3':
            l = get_valid_input("Enter length (m): ")
            w = get_valid_input("Enter width (m): ")
            t = get_valid_input("Enter thickness (m): ")
            vol = slab_volume(l, w, t)
        elif choice == '4':
            l = get_valid_input("Enter length (m): ")
            w = get_valid_input("Enter width (m): ")
            d = get_valid_input("Enter depth (m): ")
            vol = footing_volume(l, w, d)

        print("\nSelect Concrete Mix Ratio:")
        print("1. M15 (1:2:4) - General use / Footings")
        print("2. M20 (1:1.5:3) - Beams / Columns / Slabs")
        print("3. M25 (1:1:2) - Heavy-duty structural work")
        
        mix_choice = input("Enter mix choice (1-3): ").strip()
        mix_map = {'1': 'M15', '2': 'M20', '3': 'M25'}
        
        if mix_choice not in mix_map:
            print("❌ Invalid mix choice. Defaulting to M20.")
            mix_grade = 'M20'
        else:
            mix_grade = mix_map[mix_choice]

        try:
            result = calculate_materials(element_name, vol, mix_grade)
            print_report(result, mix_grade)
        except ValueError as e:
            print(f"❌ Calculation Error: {e}")


if __name__ == "__main__":
    main()
