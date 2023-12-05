using UnityEngine;
using NUnit.Framework;

[TestFixture]
public class FoodTests
{
    private GameObject testGameObject;
    private Food testFood;
    private Snake testSnake;
    private BoxCollider2D testCollider;

    // Setup method to create a test GameObject with the Food and Snake components
    [SetUp]
    public void Setup()
    {
        testGameObject = new GameObject();
        testFood = testGameObject.AddComponent<Food>();
        testSnake = testGameObject.AddComponent<Snake>();
        testCollider = testGameObject.AddComponent<BoxCollider2D>();

        testFood.gridArea = testCollider;
        testFood.snake = testSnake;

        testFood.RandomizePosition();
    }

    // Test case to check if Awake method assigns correct Snake component to the Food
    [Test]
    public void Awake_AssignsSnakeComponent()
    {
        testFood.Awake();

        Assert.IsNotNull(testFood.snake);
    }

    // Test case to check if Start method calls RandomizePosition
    [Test]
    public void Start_CallsRandomizePosition()
    {
        testFood.Start();

        Assert.IsTrue(testFood.transform.position == Vector3.zero);
    }

    // Test case to check if RandomizePosition method sets transform position within grid area
    [Test]
    public void RandomizePosition_SetsTransformPositionWithinGridArea()
    {
        Bounds bounds = testFood.gridArea.bounds;
        Vector3 position = testFood.transform.position;

        Assert.IsTrue(position.x >= bounds.min.x && position.x <= bounds.max.x);
        Assert.IsTrue(position.y >= bounds.min.y && position.y <= bounds.max.y);
    }

    // Test case to check if OnTriggerEnter2D method calls RandomizePosition
    [Test]
    public void OnTriggerEnter2D_CallsRandomizePosition()
    {
        testFood.OnTriggerEnter2D(null);

        Assert.IsTrue(testFood.transform.position == Vector3.zero);
    }
}
