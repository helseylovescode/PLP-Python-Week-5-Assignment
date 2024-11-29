# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, ram, battery_capacity):
        """
        Initialize common attributes of all smartphones.
        """
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.ram = ram  # in GB
        self.battery_capacity = battery_capacity  # in mAh

    def make_call(self, number):
        """
        Simulate making a call.
        """
        return f"Dialing {number} from {self.brand} {self.model}..."

    def send_message(self, number, message):
        """
        Simulate sending a message.
        """
        return f"Sending message to {number}: '{message}'"

    def charge(self):
        """
        Simulate charging the smartphone.
        """
        return f"Charging {self.brand} {self.model}'s battery..."

# Subclass: Samsung Galaxy S23 Ultra
class SamsungGalaxyS23Ultra(Smartphone):
    def __init__(self, color, camera_megapixels, stylus, *args, **kwargs):
        """
        Initialize the specific attributes for Samsung Galaxy S23 Ultra.
        """
        super().__init__(*args, **kwargs)  # Call the base class constructor
        self.color = color
        self.camera_megapixels = camera_megapixels  # Primary camera megapixels
        self.stylus = stylus  # Boolean indicating whether it comes with a stylus (e.g., S Pen)

    def take_picture(self):
        """
        Simulate taking a picture with the camera.
        """
        return f"Taking a photo with the {self.camera_megapixels}MP camera on {self.brand} {self.model}."

    def use_stylus(self):
        """
        Simulate using the stylus.
        """
        if self.stylus:
            return f"Using the stylus with {self.brand} {self.model}."
        else:
            return f"The {self.brand} {self.model} does not have a stylus."

    def device_info(self):
        """
        Display all the device information.
        """
        return (f"Device: {self.brand} {self.model}\n"
                f"Color: {self.color}\n"
                f"Storage: {self.storage}GB\n"
                f"RAM: {self.ram}GB\n"
                f"Battery Capacity: {self.battery_capacity}mAh\n"
                f"Camera: {self.camera_megapixels}MP\n"
                f"Stylus: {'Yes' if self.stylus else 'No'}")

# Main program to create an object of Samsung Galaxy S23 Ultra
if __name__ == "__main__":
    # Creating an instance of SamsungGalaxyS23Ultra
    my_phone = SamsungGalaxyS23Ultra(
        brand="Samsung",
        model="Galaxy S23 Ultra",
        storage=512,  # 512GB storage
        ram=12,  # 12GB RAM
        battery_capacity=5000,  # 5000mAh battery
        color="Phantom Black",
        camera_megapixels=200,  # 200MP camera
        stylus=True  # Comes with S Pen
    )

    # Calling methods and printing outputs
    print(my_phone.device_info())
    print(my_phone.make_call("0781156789"))
    print(my_phone.send_message("0781156789", "Hello from my Samsung Galaxy S23 Ultra!"))
    print(my_phone.take_picture())
    print(my_phone.charge())
    print(my_phone.use_stylus())
