import inspect
import browsers, generic, utils

# This method provides a list of all browsers implemented.
# Returns a list containing implemented browser classes
def get_browsers():

    # recursively get all concrete subclasses
    def get_subclasses(browser):
        # include browser itself in return list if it is concrete
        sub_classes = []
        
        if not inspect.isabstract(browser):
            sub_classes.append(browser)

        for sub_class in browser.__subclasses__():
            sub_classes.extend(get_subclasses(sub_class))
        
        return sub_classes

    return get_subclasses(generic.Browser)

# Method used to obtain browser histories of all available and supported browsers for the system platforms.
def get_history():
    output_object = generic.Outputs(fetch_type="history")
    browser_classes = get_browsers()
    for browser_class in browser_classes:
        try:
            browser_object = browser_class()
            browser_output_object = browser_object.fetch_history()
            output_object.histories.extend(browser_output_object.histories)
        
        except AssertionError:
            utils.logger.info("%s browser is not supported", browser_class.name)
    
    output_object.histories.sort()
    
    return output_object
