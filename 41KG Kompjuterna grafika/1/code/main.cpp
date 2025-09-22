#include <iostream>
#include <GLFW/glfw3.h>

float convertColorFromIntToFloatRange(int colorValueRGB, int oldMin=0, int oldMax=255) {
	float newMin = 0.0f;
	float newMax = 1.0f;

	int oldRange = oldMax - oldMin;
	float newRange = newMax - newMin;
	float newValue = (((colorValueRGB - oldMin) * newRange) / oldRange) + 0;
	return newValue;
}

int main() {
	// Запустити GLFW
	if (!glfwInit()) {
		std::cerr << "Failed to initialize GLFW" << std::endl;
		return -1;
	}

	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	char windowTitle[] = "CI41 Computer Graphics 1: OpenGL Window";
	GLFWwindow* window = glfwCreateWindow(800, 600, windowTitle, NULL, NULL);
	if (!window) {
		std::cerr << "Failed to make a GLFW window" << std::endl;
		glfwTerminate();
		return -1;
	}

	glfwMakeContextCurrent(window);
	std::cout << "OpenGL version: " << glGetString(GL_VERSION) << std::endl;

	float redValue = convertColorFromIntToFloatRange(178);
	float greenValue = convertColorFromIntToFloatRange(51);
	float blueValue = convertColorFromIntToFloatRange(255);

	while (!glfwWindowShouldClose(window)) {
		glfwPollEvents();
		glClearColor(redValue, greenValue, blueValue, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT);
		glfwSwapBuffers(window);
	}

	glfwDestroyWindow(window);
	glfwTerminate();
	return 0;
}