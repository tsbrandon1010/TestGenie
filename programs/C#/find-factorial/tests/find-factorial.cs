java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class FactorialTest {
    
    @Test
    public void testFactorialWithZero() {
        int expected = 1;
        int actual = Factorial(0);
        assertEquals(expected, actual);
    }
    
    @Test
    public void testFactorialWithPositiveNumber() {
        int expected = 120;
        int actual = Factorial(5);
        assertEquals(expected, actual);
    }
    
    @Test
    public void testFactorialWithNegativeNumber() {
        int expected = 1;
        int actual = Factorial(-5);
        assertEquals(expected, actual);
    }
}
