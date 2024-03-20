
**原教程是基于 UE 4.18，我是基于 UE 4.25**

[英文原地址](https://link.juejin.cn/?target=https%3A%2F%2Funrealcpp.com%2Fcharacter-bind-button%2F "https://unrealcpp.com/character-bind-button/")

在本教程中，让我们为角色添加一个 **Action** 键盘响应。首先，我们需要添加一个名为 **Action** 的输入选项，并将其绑定到键盘输入或控制器按钮上。在本例中，我们将把 Action 输入绑定到键盘的 **F** 键。转到 **编辑->项目设置（Edit -> Project Settings）** 。然后选择 **Input** 选项。单击 **Action Mappings** 旁边的加号。调用新的输入 **Action** 并从下拉菜单中选择 **F** 。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/826b0bea398f4aee9ab739f75e6ead01~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)​

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/816d6f212b3844089b6db8fd6727f0d2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)​

 在 **xxxCharacter.h** 文件中，在 `OnFire` 方法下添加 `OnAction` 方法。

```
protected:
	
	/** Fires a projectile. */
	void OnFire();

	// on action 
	void OnAction();

```

接下来，在 **xxxCharacter.cpp** 文件中，我们将找到 `SetupPlayerInputComponent` 函数，并将 **Action** 映射与 `OnAction` 函数连接起来。我们之后马上会创建 `OnAction` 函数。

我通过 `PlayerInputComponent` 中 的 `BindAction` 函数将控制器连接到 `OnAction` 函数。在这个例子中，每次按下键盘 **F** 时都会调用 `OnAction` 函数

```
PlayerInputComponent->BindAction("Action", IE_Pressed, this, &AUnrealCPPCharacter::OnAction);

```

最后，我们将添加 **OnAction** 函数。这将是一个非常简单的函数，用于将消息记录到屏幕上。

```
void AUnrealCPPCharacter::OnAction() 
{
	if (GEngine) 
	{
            GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Red, TEXT("I'm Pressing Action"));
	}
}

```

游戏运行后，按下 **F** 键的效果图如下 

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9c5449a15534cf498a3f44ed551b1e9~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)​

  

本文转自 [https://juejin.cn/post/6990105727301845028?searchId=2024032014133568FACAE16FDA0723DACC](https://juejin.cn/post/6990105727301845028?searchId=2024032014133568FACAE16FDA0723DACC)，如有侵权，请联系删除。