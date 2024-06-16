import reflex as rx
from reflex.vars import Var


# INDEX PAGE SPLINE
class Spline_Index(rx.Component):
    """
    This class represents a Spline component that can be used in a personal website.
    It provides the necessary attributes and methods to interact with the Spline tool.

    Attributes:
        library (str): The library used for the Spline component.
        tag (str): The tag associated with the Spline component.
        scene (str): The URL of the Spline scene.
        is_default (bool): Indicates if the Spline component is the default one.
        lib_dependencies (list[str]): The list of library dependencies for the Spline component.
    """

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = "https://prod.spline.design/kbccWev3xSCWPj50/scene.splinecode"
    is_default = True
    lib_dependencies: list[str] = ["@splinetool/runtime"]


spline_index = Spline_Index.create


def spline_component_index_page() -> rx.Component:
    """
    Returns a Chakra UI component for the index page of the spline component.

    Returns:
        rx.Component: The Chakra UI component for the index page.
    """
    return rx.chakra.center(
        rx.chakra.center(
            spline_index(),
            width="30em",
            height="30em",
        ),
        width="100%",
        display=["none", "none", "none", "none", "flex", "flex"],
    )
