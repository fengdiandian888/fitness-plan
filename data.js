/* ============================================================
   减脂计划 · 共享数据源 v3.0
   装备：拉力绳 + 瑜伽垫 + 跳绳 + 2×20KG 可组合哑铃（可做杠铃）
   适用人群：男性 · 170cm · 83.25kg · 新手 · 肩袖需要保护
   ============================================================ */

// ============ 核心指标（所有页面唯一来源）============
const FIT = {
  metrics: {
    protein: 110,       // 每日蛋白质目标（g）大体重需更高
    proteinBreakfast: 30,
    proteinLunch: 25,
    proteinDinner: 55,
    water: '3.0L',
    waterCount: 6,
    waterPer: '500ml',
    sleepHours: 7.5,
    sleepBed: '23:30',
    sleepWake: '07:00',
    exercise: '75′'
  },
  body: {
    gender: '男',
    height: 170,
    weight: 83.25,
    startWeight: 85,
    bmi: 28.7,
    targetMin: 68,
    targetMax: 72,
    location: '株洲 · 石峰区',
    commute: '小电动通勤'
  },

  // ============ 装备信息 ============
  equipment: {
    dumbbells: '2×20KG 可组合哑铃（可组合成短杠铃）',
    resistanceBand: '拉力绳/弹力带',
    jumpRope: '跳绳',
    yogaMat: '瑜伽垫',
    note: '新手阶段哑铃单手握持建议 5–10KG，随适应逐步加量'
  },

  // ============ 晚餐默认配比 ============
  dinner: {
    protein: '260g',
    veg: '300g',
    carb: '50g 内',
    proteinOpts: '鸡胸肉 / 瘦牛肉（腿日用牛肉）/ 鱼虾',
    vegOpts: '黄瓜 / 丝瓜 / 菠菜 / 生菜 / 苋菜 / 西红柿',
    carbOpts: '半根玉米 80g / 小块南瓜 200g / 半个红薯 100g',
    note: '不吃西兰花'
  },

  // ============ 每日标签 & 训练类型 ============
  dayLabels: ['纯恢复日', '拉日训练', '有氧+核心', '推日训练', '有氧+核心', '腿日训练', '全身哑铃+跳绳'],
  dayKeys:   ['recovery',    'pull',      'cardio',    'push',     'cardio',    'leg',       'fullbody'],

  // ============ 里程碑 ============
  milestones: [
    { wt: 85, label: '起点',   time: '' },
    { wt: 80, label: '',       time: '3–4 周' },
    { wt: 76, label: '',       time: '6–8 周' },
    { wt: 72, label: '',       time: '10–14 周' },
    { wt: 68, label: '目标',   time: '18–22 周' }
  ],

  // ============ 天气 ============
  weather: {
    city: 'Zhuzhou',
    url: 'https://wttr.in/Zhuzhou?format=j1',
    cacheKey: 'fit_wx_cache',
    cacheTTL: 30 * 60 * 1000
  }
};

/* ============================================================
   视频链接注册表（v3.4 B站+YouTube+GIF三平台）
   合并 jf-1 的 B 站视频数据 + MuscleWiki YouTube 视频 + GIF 动画
   ============================================================ */
FIT.vids = {
  // === MuscleWiki 动作示范（YouTube视频 + GIF动画）===
  mwRow:              { yt: 'H72k2iGxX_g', gif: 'https://aka.doubaocdn.com/s/lcop1wgc8P', title: 'MuscleWiki · 哑铃单臂划船', plays: '113K subs', note: 'Master Your Single Arm Dumbbell Row · Perfect Form Tips' },
  mwLateralRaise:     { yt: 'TOKQbh6FPkU', gif: 'https://aka.doubaocdn.com/s/NkZV1wgc8a', title: 'MuscleWiki · 哑铃侧平举', plays: '113K subs', note: 'Mastering the Lateral Raise · Tips for Rounder Delts' },
  mwBicepGuide:       { yt: 'Fci4s0CC0mE', gif: 'https://aka.doubaocdn.com/s/SLZW1wgc8a', title: 'MuscleWiki · 二头肌训练指南 2026', plays: '113K subs', note: 'The 2026 Bicep Training Guide · Anatomy → Angles → Sets/Reps' },
  mwBenchPress:       { gif: 'https://aka.doubaocdn.com/s/gbWH1wgc8E', title: 'MuscleWiki · 哑铃卧推', note: 'Dumbbell Bench Press · Chest Exercise' },
  mwGobletSquat:      { gif: 'https://aka.doubaocdn.com/s/SbOn1wgc8Z', title: 'MuscleWiki · 哑铃酒杯深蹲', note: 'Dumbbell Goblet Squat · Leg Exercise' },
  mwOverheadPress:    { gif: 'https://aka.doubaocdn.com/s/1VMB1wgc8P', title: 'MuscleWiki · 哑铃肩推', note: 'Dumbbell Overhead Press · Shoulder Exercise' },
  mwBulgarianSplit:   { gif: 'https://aka.doubaocdn.com/s/RFuz1wgc93', title: 'MuscleWiki · 保加利亚分腿蹲', note: 'Bulgarian Split Squat · Leg Exercise' },
  mwRDL:              { gif: 'https://aka.doubaocdn.com/s/hcnl1wgc93', title: 'MuscleWiki · 哑铃罗马尼亚硬拉', note: 'Dumbbell Romanian Deadlift · Hamstring Exercise' },
  mwTricepExt:        { gif: 'https://aka.doubaocdn.com/s/YSZQ1wgc93', title: 'MuscleWiki · 哑铃三头肌伸展', note: 'Dumbbell Skullcrusher · Tricep Exercise' },
  
  // === B站视频（完整跟练）===
  shoulderRehab:       { bv: 'BV1WM411U7yq', title: '倍他运动康复 · 肩袖弹力带', plays: '99万' },
  rehabShoulderDaily:  { bv: 'BV1WM411U7yq', title: '肩袖康复弹力带跟练', plays: '' },
  shoulderWarmup:      { bv: 'BV1E2RkBWEFs', title: '骨科康复师 · 上肢完整热身', plays: '' },

  morningCardio:       { bv: 'BV1e541197y8', title: '刘畊宏 · 18分钟晨间暖身训练', plays: '254.6万', note: '提高代谢·运动前提升心率' },
  lowImpactBriskWalk:  { bv: 'BV1KH4y137xv', title: '游书庭 · 30分钟无跳跃有氧HIIT', plays: '277万', note: '大体重/新手·无跳跃·膝盖友好' },
  lowImpactFullbody:   { bv: 'BV1pr4y1t7BZ', title: '刘畊宏 · 30分钟有氧快乐健身操', plays: '1459.8万', note: '附带拉伸·无剧烈运动·男女皆宜' },
  hiitLowImpact:       { bv: 'BV1KH4y137xv', title: '游书庭 · 30分钟无跳跃HIIT', plays: '277万', note: '大体重/新手友好·零跳跃' },
  cyclingIndoor:       { bv: 'BV182eRzuEKL', title: '游书庭 · 30分钟站立式全身燃脂', note: '零跳跃·不伤膝盖·简单有效' },

  morningCore:         { bv: 'BV182eRzuEMD', title: '游书庭 · 20分钟瘦腰腹核心', note: '全程站立·无跳跃·大体重友好' },
  morningYoga:         { bv: 'BV1gVLFzBEBN', title: '张德琪 · 6分钟晨间柔韧拉伸', plays: '' },
  stretchEleni:        { bv: 'BV1Eu41187oU', title: '凯圣王 · 躯干拉伸', plays: '21.7万', note: '7′41″·新手增肌系列·运动后必做' },
  stretchAlt:          { bv: 'BV1shM2eTEhW', title: '游书庭 · 6分钟收操拉伸', note: '训练后·全身放松舒展' },
  stretchAltLong:      { bv: 'BV1skaizGEqH', title: '暴躁小细菌 · 40′全身拉伸', plays: '' },
  foamRoller:          { bv: 'BV1wY4y1h7Bd', title: '健身普拉斯 · 40分钟全身泡沫轴', plays: '' },

  pullMorning:         { bv: 'BV18jxRznELd', title: '梅林FIT · 三分化4.0 拉日', plays: '' },
  pullWorkout:         { bv: 'BV1uZ42127Gz', title: '梅林FIT · 二分化拉日 哑铃增肌', plays: '12.8万', note: '52′·一对哑铃·背+二头·新手时间少首选', dbType: true },
  pushMorning:         { bv: 'BV1LhnmzFEEa', title: '梅林FIT · 三分化4.0 推日', plays: '' },
  pushWorkout:         { bv: 'BV1qF4m1M7rL', title: '梅林FIT · 二分化推日 哑铃增肌', plays: '34万', note: '51′45″·一对哑铃·胸+三头·肩安全关注', dbType: true },
  legMorning:          { bv: 'BV1FusRzAEYv', title: '梅林FIT · 三分化4.0 腿日', plays: '' },
  legWorkout:          { bv: 'BV1RW42197ez', title: '梅林FIT · 三分化 哑铃增肌 肩+臀腿', plays: '33.6万', note: '66′30″·哑铃臀腿·收藏1.6万·一步到位', dbType: true },
  fullbodyDumbbell:    { bv: 'BV11cmmYeED4', title: '梅林FIT · 20分钟哑铃全身塑形', plays: '9.3万', note: '21′·轻量哑铃·周六维持日·新手友好', dbType: true },
  coreTabata:          { bv: 'BV182eRzuEMD', title: '游书庭 · 20分钟瘦腰腹核心', note: '全程站立·无跳跃·大体重友好' },

  pullTheory:          { bv: 'BV18jxRznELd', title: '梅林FIT · 三分化4.0 拉日', plays: '' },
  pushTheory:          { bv: 'BV1LhnmzFEEa', title: '梅林FIT · 三分化4.0 推日', plays: '' },
  legTheory:           { bv: 'BV1FusRzAEYv', title: '梅林FIT · 三分化4.0 腿日', plays: '' },

  pullBandAlt:         { bv: 'BV162421N7Xs', title: '梅林FIT · 弹力绳三分化 背+二头', plays: '5.5万', note: '45′59″·弹力绳备选版' },
  pushBandAlt:         { bv: 'BV16SGH6aEyU', title: '阿龙新手健身 · 居家三分化 胸+三头', note: '13′49″·无器械·弹力绳备选' },
  legBandAlt:          { bv: 'BV15C41137dN', title: '梅林FIT · 弹力绳三分化 肩+臀腿', plays: '3.5万', note: '47′42″·弹力绳备选版' },
  sundayStretch:       { bv: 'BV1MjXZBGEVt', title: '阿见见 · 20分钟拉伸全身', plays: '' },
  theoryNewbie:        { bv: 'BV1Hk4y187jF', title: '好人松松 · 健身新手训练完全手册', plays: '' },
  warmupSaturday:      { bv: 'BV1DbM2eKEe2', title: '游书庭 · 5分钟暖身操', plays: '3.8万', note: '5′26″·居家运动前必做·唤醒肌肉' },
  cardioAltMizi:       { bv: 'BV1pr4y1t7BZ', title: '刘畊宏 · 30分钟有氧快乐健身操', note: '附带拉伸·男女皆宜' },
  cardioAltEleni:      { bv: 'BV1bz411b7HH', title: '闫帅奇 · 健身前全身热身训练', plays: '71.2万', note: '5′53″·收藏向·激活全身' },
  bandFullBody:        { bv: 'BV1ZT4y1U7vX', title: 'Erik埃里克 · 弹力带全身训练', plays: '180万', note: '19′49″·无跳跃·膝盖友好·周六维持日' },
  pushBandPro:         { bv: 'BV1VF4m1L7Mb', title: '梅林FIT · 弹力绳三分化 胸+三头', plays: '5.3万', note: '50′56″·完整跟练·弹力绳推日' }
};

/* ============================================================
   训练计划（v3.1 全哑铃版 + 新手保护）
   关键调整：
   1. 推日用「哑铃卧推/上斜推」替代俯卧撑（保护肩腕）
   2. 拉日用「哑铃划船 + 哑铃面拉」替代弹力带动作
   3. 腿日用「哑铃酒杯深蹲 + 分腿蹲」降低膝盖压力
   4. 肩袖保护用「哑铃肩外旋」替代弹力带肩外旋
   5. 每周 5 天训练 + 2 天恢复，不急躁
   ============================================================ */
FIT.plans = {
  pull: {
    title: '拉日训练 · 背 + 二头 + 后束',
    focus: '背部厚度 + 二头 + 肩后束（改善圆肩）',
    color: 'pull',
    moves: [
      { name: '哑铃俯身划船（主项）', sets: '4 × 10–12', rest: '90s', image: 'bent-over-row.jpg', video: 'https://www.douyin.com/search/%E5%93%81%E9%9B%B6%E5%89%8D%E4%BC%B8%E5%88%92%E8%87%AA%E6%9B%B4%E6%95%99%E5%AD%A6',
        steps: [
          '① 准备姿势：双脚与肩同宽站立，哑铃握距与肩同宽或略宽，掌心朝向身体',
          '② 屈髋屈膝：臀部向后推，上身前倾约 45°，背部保持平直，腰椎自然中立',
          '③ 起始位置：手臂伸直下垂，哑铃位于膝盖正下方或略前',
          '④ 发力拉起：以背阔肌收缩为主导发力，肘部贴近身体向臀部方向拉起',
          '⑤ 顶峰收缩：在最高点停顿 1–2 秒，感受两块肩胛骨向中间夹紧，背部强烈收缩',
          '⑥ 缓慢下放：控制离心阶段 2–3 秒，哑铃沿原路径缓慢下放，保持肌肉张力',
          '⑦ 呼吸节奏：拉起时呼气，下放时吸气，全程保持核心收紧不塌腰'
        ],
        tips: '💡 发力感：集中在背部中间位置（背阔肌）；常见错误：身体晃动借力、耸肩、肘部外展过大',
        weight: '新手建议 5–10kg，熟悉后逐步加量'
      },
      { name: '哑铃俯身划船（双臂版）', sets: '3 × 12–15', rest: '75s', image: 'bent-over-row.jpg', video: 'https://www.douyin.com/search/%E5%93%81%E9%9B%B6%E5%89%8D%E4%BC%B8%E5%88%92%E8%87%AA%E6%9B%B4%E6%95%99%E5%AD%A6',
        steps: [
          '① 准备姿势：双脚与肩同宽站立，双手各握哑铃，掌心朝内（中立握法）',
          '② 屈髋俯身：臀部向后推，上身前倾约 45°，背部保持平直，腰椎自然中立',
          '③ 起始位置：手臂伸直下垂，哑铃位于膝盖正下方，肩胛骨放松下沉',
          '④ 发力拉起：以背阔肌收缩为主导，肘部贴近身体向臀部方向拉起',
          '⑤ 顶峰收缩：在最高点停顿 1 秒，感受两块肩胛骨向中间夹紧，背部强烈收缩',
          '⑥ 缓慢下放：控制 2–3 秒，哑铃沿原路径缓慢下放，保持肌肉张力',
          '⑦ 呼吸节奏：拉起时呼气，下放时吸气，全程保持核心收紧不塌腰'
        ],
        tips: '💡 双臂版与单臂版区别：双臂版更侧重整体背部厚度，单臂版更能纠正左右不平衡；常见错误：身体晃动借力、耸肩、肘部外展过大',
        weight: '新手建议 5–10kg，比单臂版轻 2–3kg，保证动作标准'
      },
      { name: '哑铃面拉', sets: '3 × 15', rest: '60s', image: 'lateral-raise.jpg', video: 'https://www.douyin.com/search/%E5%93%81%E9%9B%B6%E9%9D%A2%E6%8B%89%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 准备姿势：站姿，双脚与肩同宽，双手各握轻量哑铃，掌心相对',
          '② 起始位置：手臂伸直向前举起至与肩平，哑铃位于胸前前方',
          '③ 向后拉动：以肩后束发力，手臂向面部两侧弧形拉开，肘部保持微屈',
          '④ 手腕旋转：拉动过程中手腕逐渐旋前，掌心向下，形成「拉锯」动作',
          '⑤ 顶峰位置：肘部抬高至肩膀水平或略高，指尖指向后方',
          '⑥ 停顿挤压：保持 1 秒，感受肩后束和上背菱形肌强烈收缩',
          '⑦ 控制还原：缓慢控制将哑铃还原到起始位置，保持张力不松劲'
        ],
        tips: '💡 关键点：这个动作是改善圆肩的黄金动作，每个动作都要认真感受肩后束发力；常见错误：只用前臂力量、肘部下沉、耸肩',
        weight: '用轻重量，建议 2–5kg，重点是感受肌肉发力而非重量'
      },
      { name: '哑铃硬拉（罗马尼亚式）', sets: '3 × 8–10', rest: '90s', image: 'deadlift.jpg', video: 'https://www.douyin.com/search/%E7%BD%97%E4%B8%81%E9%87%8C%E4%BA%9A%E5%BC%B9%E6%8B%89%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 站距调整：双脚与髋同宽站立，脚尖朝前，哑铃置于大腿前侧',
          '② 屈髋启动：保持膝盖角度基本不变（微屈 15–20°），以髋关节为铰链前倾',
          '③ 哑铃路径：哑铃沿腿前侧（贴近大腿）缓慢下放，保持贴近不远离',
          '④ 下放终点：下至感觉到腘绳肌（大腿后侧）有明显拉伸感即可，不必追求过低',
          '⑤ 挤压臀部：发力时脚跟踩实地面，臀部向前推，收紧臀大肌站直',
          '⑥ 顶峰收缩：站直后在顶部用力夹紧臀部 1 秒，但不要过度挺腰后仰',
          '⑦ 呼吸配合：下放时吸气、收紧核心，起立时呼气用力'
        ],
        tips: '💡 区别：这个动作不同于传统硬拉，膝盖弯曲角度固定，主要拉伸腘绳肌而非股四；常见错误：弓背、腰椎过度伸展、膝盖过于弯曲',
        weight: '从 5kg 开始，重点是找到腘绳肌拉伸和发力的感觉'
      },
      { name: '哑铃弯举（二头肌）', sets: '3 × 12', rest: '60s', image: 'bicep-curl.jpg', video: 'https://www.douyin.com/search/%E5%93%81%E9%9B%B6%E5%AE%A4%E4%B8%BE%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 站姿准备：双脚与肩同宽，双手各握哑铃，掌心朝前（旋前位）',
          '② 起始位置：手臂自然下垂，大臂贴近身体两侧，肘部位置固定不动',
          '③ 弯举动作：以二头肌发力带动小臂向上弯举，哑铃向肩部方向移动',
          '④ 顶峰收缩：在最高点停顿 1 秒，二头肌完全收紧，手腕保持中立不内旋',
          '⑤ 缓慢下放：用 2–3 秒控制哑铃缓慢下放回起始位置，保持二头肌张力',
          '⑥ 呼吸节奏：弯举时呼气，下放时吸气',
          '⑦ 避免借力：全程大臂位置不变，不前后摆动身体借力'
        ],
        tips: '💡 增加难度：可做锤式弯举（掌心相对），更多锻炼肱肌；常见错误：大臂移动、前倾借力、耸肩',
        weight: '选择 5–7.5kg，动作标准比重量更重要'
      },
      { name: '哑铃肩外旋（肩袖保护）', sets: '2 × 15', rest: '30s', image: 'rotator-cuff.jpg', video: 'https://www.douyin.com/search/%E5%93%81%E9%9B%B6%E8%82%A9%E5%A4%96%E6%97%8B%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 准备姿势：坐姿或站姿，上臂夹紧身体侧方，肘部弯曲 90°',
          '② 握铃姿势：双手各握轻量哑铃，掌心朝向身体中央（前臂垂直向下）',
          '③ 起始位置：上臂固定不动，前臂自然下垂，哑铃位于身体侧前方',
          '④ 旋转动作：以前臂为杠杆，外旋肩关节，使拳头从朝向身体中央转向朝外',
          '⑤ 旋转范围：旋转至前臂与身体呈 60–90° 角即可，不要过度旋转',
          '⑥ 顶峰停顿：保持 1 秒，感受肩袖肌群（小圆肌、冈下肌）强烈收缩',
          '⑦ 重要提示：全程上臂保持贴紧身体不动，只让前臂旋转'
        ],
        tips: '💡 必做原因：肩袖肌群薄弱是肩关节疼痛的主要原因，这个动作每次训练必做；常见错误：上臂离开身体、耸肩、用力过猛',
        weight: '用最轻的哑铃（1–3kg），目的是激活和强化而非负重'
      }
    ],
    warmup: 'shoulderWarmup',
    theory: 'pullTheory',
    main:   'pullWorkout',
    cardioAfter: 'morningCardio',
    stretch: 'stretchEleni'
  },
  push: {
    title: '推日训练 · 胸 + 肩 + 三头',
    focus: '哑铃卧推（替俯卧撑）+ 肩推 + 三头',
    color: 'push',
    moves: [
      { name: '哑铃卧推（主项）', sets: '4 × 10–12', rest: '90s', image: 'dumbbell-bench-press.jpg', video: 'https://www.douyin.com/search/%E5%93%81%E9%9B%B6%E5%8卧推训练',
        steps: [
          '① 仰卧准备：平躺在瑜伽垫上，屈膝，双脚踩实地面，臀部和后背紧贴垫子',
          '② 握铃姿势：双手各握哑铃，举至胸部上方，掌心朝脚的方向（相对或略外旋）',
          '③ 角度调整：大臂与身体呈 45–60° 角（不完全贴地也不完全张开），肘部不要外展 90°',
          '④ 下放动作：控制哑铃缓慢下放，下至哑铃位于胸部外侧，高度与乳头平齐',
          '⑤ 下放时间：下放过程保持 2 秒，全程肌肉张力不松，感受胸肌被拉长',
          '⑥ 向上推起：以胸肌收缩为主导发力，将哑铃推起至手臂伸直但肘关节不完全锁死',
          '⑦ 呼吸配合：下放时吸气，推起时呼气，推起到顶点时胸肌顶峰收缩 1 秒'
        ],
        tips: '💡 发力感：集中在胸部中间位置；常见错误：臀离开垫子、腰椎过度弓起（大重量时系腰带保护）、肘部外展 90° 伤肩、肩胛不稳',
        weight: '新手建议 5–10kg，躺在瑜伽垫上比卧推凳更稳定'
      },
      { name: '哑铃上斜推（胸肌上部）', sets: '3 × 10–12', rest: '90s', image: 'incline-dumbbell-press.jpg', video: 'https://www.douyin.com/search/%E4%B8%8A%E6%96%9C%E5%93%81%E9%9B%B6%E6%8E%A8%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 垫高上背：将枕头/垫子/折叠的瑜伽垫垫在上背部下方，形成 15–30° 的上斜角度',
          '② 仰卧姿势：头部躺在垫子边缘外（不枕枕头），双脚踩实地面',
          '③ 握铃位置：双手握哑铃举至胸部上方，掌心朝脚的方向',
          '④ 下放控制：控制哑铃缓慢下放，下至哑铃位于锁骨下方或上胸部两侧',
          '⑤ 推起发力：胸肌上部发力推起哑铃，想象用「锁骨去顶天花板」的感觉',
          '⑥ 顶峰收缩：在最高点停顿 1 秒，胸肌上部强烈收缩',
          '⑦ 注意事项：角度不宜过高（不超过 45°），否则肩部压力过大'
        ],
        tips: '💡 角度选择：角度越高胸肌上部参与越多，但肩部压力越大，建议 15–30°；常见错误：凳子角度太高、耸肩推起、腰椎过度弓起',
        weight: '新手建议 3–5kg，比平板卧推更轻，因为单关节稳定性更差'
      },
      { name: '哑铃侧平举（中束）', sets: '3 × 15', rest: '60s', image: 'lateral-raise.jpg', video: 'https://www.douyin.com/search/%E5%93%81%E9%9B%B6%E4%BE%A7%E5%B9%B3%E4%B8%BE%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 起始姿势：站立，双脚与肩同宽，双手各握哑铃置于大腿前侧',
          '② 身体姿态：挺胸收腹，肩部下沉不耸肩，想象肩部被绳子向下拉',
          '③ 抬臂动作：以肘部为引导点，微弯肘关节（保持 10–15° 屈角），向身体两侧抬起',
          '④ 抬起高度：抬至手臂与地面平行即可，不必追求过高（与肩平或略低于肩）',
          '⑤ 顶峰位置：在最高点停顿 1 秒，手臂略低于肘关节，形成「倒水」姿势（小指高于拇指）',
          '⑥ 缓慢下放：用 2–3 秒控制哑铃缓慢下放回起始位置，保持肌肉张力',
          '⑦ 全程控制：手臂不要完全伸直锁死，下放时不要让哑铃弹回大腿'
        ],
        tips: '💡 发力感：集中在肩部中束（三角肌中束）；常见错误：耸肩借力、手臂完全伸直、下放太快、重量过大导致上斜方肌代偿',
        weight: '必须用轻重量，建议 2–5kg，新手可从 1–2kg 哑铃甚至矿泉水瓶开始'
      },
      { name: '哑铃俯身臂屈伸（三头）', sets: '3 × 12', rest: '60s', image: 'tricep-pushdown.jpg', video: 'https://www.douyin.com/search/%E4%B8%89%E5%A4%B4%E8%87%AA%E6%9B%B4%E6%95%99%E5%AD%A6',
        steps: [
          '① 身体姿态：站立，一只手支撑在同侧膝盖上，或支撑在凳子/椅子上，保持躯干前倾约 45°',
          '② 起始位置：持哑铃的上臂平行于地面（垂直于躯干），前臂自然下垂垂直于地面',
          '③ 保持位置：收紧核心，全程保持上臂固定不动，不随前臂移动',
          '④ 伸展动作：以三头肌发力，将前臂向后上方伸展，直到手臂接近伸直',
          '⑤ 顶峰收缩：在最高点停顿 1 秒，三头肌强烈收缩',
          '⑥ 缓慢还原：控制 2 秒缓慢还原到起始位置，三头肌全程保持张力',
          '⑦ 两侧交替：完成一组后换另一侧，或按哑铃数量交替完成'
        ],
        tips: '💡 替代方案：如站立不稳，可坐姿进行；常见错误：上臂随前臂移动（甩动借力）、耸肩、躯干过度前倾',
        weight: '3–5kg 即可，重点是三头发力而非重量'
      },
      { name: '墙壁天使（肩关节活动）', sets: '2 × 10', rest: '45s', image: 'rotator-cuff.jpg', video: 'https://www.douyin.com/search/%E5%A2%99%E5%A3%81%E5%A4%A9%E4%BD%BF%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 靠墙站立：后脑勺、上背部、臀部贴墙，脚跟离墙约 10cm',
          '② 手臂姿势：屈肘 90°，上臂与前臂贴墙，手肘高度与肩膀平齐',
          '③ 起始位置：保持手臂贴墙，将手臂向上滑动至头顶，手臂全程贴墙',
          '④ 动作过程：手臂沿墙面缓慢向上「游泳」，感受肩胛骨在背部滑动',
          '⑤ 最高位置：手臂举至头顶，肩胛骨充分向上旋转',
          '⑥ 缓慢返回：控制 3–5 秒缓慢将手臂滑回起始位置',
          '⑦ 重复动作：保持手臂全程贴墙，重复 10 次'
        ],
        tips: '💡 改善圆肩：这个动作能有效打开胸椎、改善肩关节活动度；常见错误：手臂离开墙面、腰椎离开墙面、耸肩',
        weight: '徒手进行，重点是动作控制和肩关节活动'
      }
    ],
    warmup: 'shoulderWarmup',
    theory: 'pushTheory',
    main:   'pushWorkout',
    cardioAfter: 'hiitLowImpact',
    stretch: 'stretchEleni'
  },
  leg: {
    title: '腿日训练 · 腿 + 臀 + 小腿',
    focus: '哑铃酒杯深蹲 + 分腿蹲 + 直腿硬拉',
    color: 'leg',
    moves: [
      { name: '哑铃酒杯深蹲（主项）', sets: '4 × 12–15', rest: '90s', image: 'goblet-squat.jpg', video: 'https://www.douyin.com/search/%E9%85%92%E6%9D%AF%E6%8B%9B%E8%B7%83%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 站距准备：双脚与肩同宽或略宽，脚尖可略微外展（不超过 30°）',
          '② 握铃姿势：双手托住哑铃一端，举至胸前（杯式握法），肘部朝向膝盖方向',
          '③ 屈髋屈膝：臀部向后「坐」的同时，膝盖弯曲，身体垂直下降',
          '④ 下蹲深度：蹲至大腿与地面平行或略低（量力而行），膝盖不超过脚尖太多',
          '⑤ 膝盖方向：膝盖方向与脚尖方向一致，不要内扣，全程保持膝盖稳定',
          '⑥ 起身发力：以脚跟和前脚掌发力蹬地，臀部向前推，伸直双腿站起',
          '⑦ 顶峰站立：在顶部用力收紧臀部 1 秒，但不要过度挺腰'
        ],
        tips: '💡 保护膝盖：下蹲时膝盖方向与脚尖一致可减少膝盖剪切力；常见错误：膝盖内扣、腰椎过度弯曲、重心在前脚掌',
        weight: '新手建议 5–10kg，10–15kg 是进阶重量；放在胸前还有助保持直背上身'
      },
      { name: '保加利亚分腿蹲', sets: '3 × 10/侧', rest: '90s', image: 'split-squat.jpg', video: 'https://www.douyin.com/search/%E4%BF%9D%E5%8A%A0%E5%88%A9%E4%BA%9A%E5%88%86%E8%85%BF%E8%B7%83%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 起始站姿：站在椅子/台阶前，距离约一脚掌长度，面朝前方',
          '② 后腿位置：后腿脚背搭在椅子/台阶上，脚尖触地或脚背贴实',
          '③ 前腿支撑：身体重心放在前腿上，双手各握哑铃或叉腰',
          '④ 下蹲动作：屈前腿膝关节，降低身体，直到后腿膝盖接近地面',
          '⑤ 下蹲深度：前腿大腿与地面平行或略低，后腿膝盖几乎触地',
          '⑥ 起身发力：前脚跟发力蹬地，将身体推起回到起始位置',
          '⑦ 膝盖方向：全程保持前膝方向与脚尖一致，不要内扣'
        ],
        tips: '💡 单侧训练：这个动作能发现和纠正左右腿力量不平衡；常见错误：前膝过度前伸超过脚尖、后膝撞地、前脚站距过窄导致不平衡',
        weight: '可从徒手开始熟悉动作，加哑铃后 5–10kg 即可'
      },
      { name: '哑铃罗马尼亚硬拉', sets: '3 × 10–12', rest: '90s', image: 'single-leg-rdl.jpg', video: 'https://www.douyin.com/search/%E7%BD%97%E4%B8%81%E9%87%8C%E4%BA%9A%E5%BC%B9%E6%8B%89%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 站距调整：双脚与髋同宽站立，双手各握哑铃，哑铃置于大腿前侧',
          '② 膝盖角度：全程保持膝盖微屈（15–20°），这个角度固定不变',
          '③ 屈髋前倾：以髋关节为轴心，臀部向后推，上身前倾，哑铃沿腿前侧下滑',
          '④ 下放深度：下至感觉到腘绳肌有明显拉伸感，或哑铃到达小腿中下部',
          '⑤ 背部姿态：保持背部平直，腰椎自然弧度，不要弓背也不要过度挺背',
          '⑥ 起身动作：脚跟踩实地面，臀部向前推，收紧臀肌将身体拉起',
          '⑦ 顶峰收缩：站直后用力收紧臀部 1 秒，不要过度后仰'
        ],
        tips: '💡 与深蹲区别：深蹲侧重股四头肌，硬拉侧重臀部和腘绳肌；常见错误：弓背、腰椎伸展、膝盖弯曲角度变化太大',
        weight: '从 5kg 开始，感受腘绳肌拉伸和臀部发力的感觉'
      },
      { name: '单腿臀桥', sets: '3 × 15/侧', rest: '60s', image: 'single-leg-glute-bridge.jpg', video: 'https://www.douyin.com/search/%E5%8D%95%E8%87%82%E8%87%80%E6%A1%A5%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 仰卧准备：平躺在瑜伽垫上，双臂放在身体两侧，掌心向下',
          '② 起始姿势：屈膝，双脚踩实地面与肩同宽，一腿伸直抬起悬空',
          '③ 准备发力：收紧核心，锁定腰椎（后背紧贴地面不离开）',
          '④ 髋部上推：以臀肌发力，将髋部向上推起，直到身体从肩膀到膝盖呈一条直线',
          '⑤ 顶峰收缩：在最高点停顿 1–2 秒，用力夹紧臀部',
          '⑥ 缓慢下放：控制 2–3 秒将髋部缓慢下放回到起始位置',
          '⑦ 换腿进行：完成一侧后换另一侧，组间可短暂休息'
        ],
        tips: '💡 常见错误：腰椎过度弓起（骨盆前倾）、下放时髋部触地让肌肉失去张力、臀部没有收紧就推起',
        weight: '徒手进行，如需增加难度可在髋部放置哑铃或杠铃片'
      },
      { name: '站姿提踵', sets: '3 × 20', rest: '45s', image: 'calf-raise.jpg', video: 'https://www.douyin.com/search/%E7%AB%9E%E6%AD%A5%E6%8F%90%E8%B9%A1%E5%AD%A6%E4%B9%A0',
        steps: [
          '① 站立姿势：双脚与肩同宽站立，可手扶墙壁或椅子保持平衡',
          '② 起始位置：双脚全脚掌着地，重心放在前脚掌',
          '③ 向上踮起：脚跟向上抬离地面，小腿肌肉收缩，尽量抬到最高点',
          '④ 顶峰收缩：在最高点停顿 1 秒，充分收紧小腿三头肌（腓肠肌和比目鱼肌）',
          '⑤ 向下控制：缓慢控制下放，脚跟尽量低于前脚掌平面（充分拉伸小腿）',
          '⑥ 动作速度：上提 1 秒，顶峰 1 秒，下放 2–3 秒',
          '⑦ 站立位置：可以站在台阶边缘让脚跟更容易向下掉，拉伸效果更好'
        ],
        tips: '💡 增加变化：坐姿提踵更多锻炼比目鱼肌，站姿提踵更多锻炼腓肠肌；常见错误：下放太快没有拉伸、屈膝过多借力',
        weight: '手扶哑铃增加负重，5–10kg 即可'
      }
    ],
    warmup: 'stretchAlt',
    theory: 'legTheory',
    main:   'legWorkout',
    cardioAfter: 'hiitLowImpact',
    stretch: 'stretchAltLong'
  },
  cardio: {
    title: '有氧 + 核心日',
    focus: '低冲击有氧 + 核心 + 步行通勤',
    color: 'cardio',
    moves: [
      { name: '晨起低冲击有氧（跟练 25 分钟）', sets: '25 分钟', rest: '—', image: 'brisk-walk.jpg',
        steps: ['① 动作前先活动关节：肩环绕 10 次 + 髋环绕 10 次', '② 跟随视频节奏，动作幅度适中，不追求最大', '③ 全程保持呼吸均匀，不要憋气', '④ 重点部位：髋、膝、踝保持弹性', '⑤ 动作结束后立即做 5 分钟全身拉伸'] },
      { name: '核心（15 分钟跟练）', sets: '15 分钟', rest: '—', image: 'core-workout.jpg',
        steps: ['① 热身：平板支撑 20 秒 × 2 组', '② 跟随视频进行 15 分钟核心训练', '③ 卷腹：下背贴地，肩抬起，腹部发力', '④ 死虫式：核心收紧，手腿缓慢交替', '⑤ 训练结束后做腰部放松（婴儿式）'] },
      { name: '步行 / 通勤骑行', sets: '30–40 分钟', rest: '—', image: 'low-impact-cardio.jpg',
        steps: ['① 开始前 5 分钟慢速（找节奏）', '② 保持匀速，心率控制在 100–120 次/分', '③ 挺胸收腹，避免塌腰或驼背', '④ 最后 5 分钟减速，做收尾活动', '⑤ 活动后补水 500ml'] },
      { name: '哑铃肩外旋（保护）', sets: '2 × 15', rest: '30s', image: 'rotator-cuff.jpg',
        steps: ['① 坐姿或站姿，上臂夹紧身体，肘部弯曲 90°', '② 双手握轻量哑铃，掌心朝向身体中央', '③ 前臂向外旋转展开，掌心朝下前方', '④ 感受肩袖肌群（小圆肌、冈下肌）收紧', '⑤ 顶峰 1 秒，缓慢还原，全程保持上臂不动'] }
    ],
    warmup: 'stretchAlt',
    main: 'hiitLowImpact',
    core: 'morningCore',
    stretch: 'stretchEleni'
  },
  recovery: {
    title: '纯恢复日 · 拉伸 + 肩康复',
    focus: '关节活动度 + 肩袖保护 + 肌肉放松',
    color: 'recovery',
    moves: [
      { name: '全身动态拉伸（10 分钟）', sets: '10 分钟', rest: '—', image: 'stretch.jpg',
        steps: ['① 头部环绕 5 圈 + 肩环绕 10 次', '② 手臂前后摆动 15 次/侧', '③ 胸椎旋转 10 次/侧', '④ 髋环绕 10 次 + 体前屈拉伸', '⑤ 膝环绕 + 踝环绕'] },
      { name: '哑铃肩外旋（肩袖保护）', sets: '3 × 15', rest: '30s', image: 'rotator-cuff.jpg',
        steps: ['① 坐姿或站姿，上臂夹紧身体，肘部弯曲 90°', '② 双手握轻量哑铃，掌心朝向身体中央', '③ 前臂向外旋转展开', '④ 感受肩袖肌群（小圆肌、冈下肌）收紧', '⑤ 顶峰 1 秒，缓慢还原，全程保持上臂不动'] },
      { name: '墙壁天使（胸椎活动）', sets: '2 × 10', rest: '30s', image: 'rotator-cuff.jpg',
        steps: ['① 背靠墙站立，后脑、背、臀贴墙', '② 屈肘 90°，上臂与前臂贴墙', '③ 缓慢向上伸直手臂，全程贴墙', '④ 顶部停顿 1 秒', '⑤ 缓慢还原，重复'] },
      { name: '慢速散步', sets: '30–40 分钟', rest: '—', image: 'brisk-walk.jpg',
        steps: ['① 开始 5 分钟：极慢速度，找节奏', '② 中期 20–30 分钟：保持匀速，呼吸平稳', '③ 注意挺胸，避免含胸驼背', '④ 手臂自然摆动，不僵手', '⑤ 最后 5 分钟减速，做深呼吸'] }
    ],
    main: 'stretchEleni',
    rehab: 'shoulderRehab',
    foam: 'foamRoller'
  },
  fullbody: {
    title: '全身哑铃循环日',
    focus: '全身均衡复合动作刺激 + 基础代谢提升',
    color: 'fullbody',
    moves: [
      { name: '哑铃全身循环（跟练 30 分钟）', sets: '3 × 循环', rest: '60s', image: 'fullbody-dumbbell.jpg', video: 'https://www.douyin.com/search/%E5%85%A8%E8%BA%AB%E5%93%81%E9%9B%B6%E5%BE%AA%E7%8E%AF%E8%BF%90%E5%8A%A8',
        steps: ['① 热身：肩环绕 10 次 + 蹲起 10 次', '② 跟随视频循环节奏完成动作', '③ 每个动作按要求次数完成，不跳不甩', '④ 循环间休息 60 秒，补水小口', '⑤ 最后 5 分钟放松拉伸'] },
      { name: '靠墙静蹲（保护膝盖）', sets: '3 × 30-40 秒', rest: '30s', image: 'wall-sit.jpg', video: 'https://www.douyin.com/search/%E9%99%AA%E5%A2%99%E9%9D%99%E8%B7%83%E5%AD%A6%E4%B9%A0',
        steps: ['① 后背完整贴墙站立，双脚向前迈出一步', '② 缓慢下蹲至大腿微酸即可，不用蹲太深', '③ 双手可轻握哑铃放在大腿增加难度', '④ 收紧核心，保持 30-40 秒', '⑤ 缓慢起身回到站立，重复 3 组'] },
      { name: '核心（瑜伽垫）', sets: '15 分钟', rest: '—', image: 'core-workout.jpg', video: 'https://www.douyin.com/search/%E6%A0%B8%E5%BF%83%E8%BA%AB%E4%BD%93%E8%AE%AD%E7%BB%83',
        steps: ['① 平板支撑 30 秒 × 3 组', '② 卷腹 15 次 × 3 组', '③ 死虫式 12 次 × 2 组', '④ 超人式 12 次 × 2 组', '⑤ 婴儿式放松 2 分钟'] },
      { name: '哑铃肩外旋', sets: '3 × 15', rest: '30s', image: 'rotator-cuff.jpg', video: 'https://www.douyin.com/search/%E5%93%81%E9%9B%B6%E8%82%A9%E5%A4%96%E6%97%8B',
        steps: ['① 坐姿或站姿，上臂夹紧身体，肘部弯曲 90°', '② 双手握轻量哑铃，掌心朝向身体中央', '③ 前臂向外旋转展开', '④ 感受肩袖肌群（小圆肌、冈下肌）收紧', '⑤ 顶峰 1 秒，缓慢还原，全程保持上臂不动'] }
    ],
    main: 'fullbodyDumbbell',
    core: 'coreTabata',
    rehab: 'rehabShoulderDaily'
  },

  // —— 可选专项日（按需替换）——
  rehabDay: {
    title: '肩/颈/腰康复日（可选）',
    focus: '肩袖 + 颈椎 + 腰椎 养护',
    color: 'recovery',
    moves: [
      { name: '哑铃肩外旋', sets: '3 × 15', rest: '30s', image: 'rotator-cuff.jpg' },
      { name: '墙壁天使', sets: '2 × 10', rest: '30s', image: 'rotator-cuff.jpg' },
      { name: '颈椎放松（自我按压）', sets: '5 分钟', rest: '—', image: 'stretch.jpg' },
      { name: '泡沫轴 · 腰背', sets: '10 分钟', rest: '—', image: 'foam-roller.jpg' },
      { name: '单腿站立平衡', sets: '3 × 30s/侧', rest: '30s', image: 'brisk-walk.jpg' }
    ],
    main: 'rehabShoulderDaily',
    rehab: 'shoulderRehab',
    foam: 'foamRoller'
  },
  coreDay: {
    title: '核心强化日（可选）',
    focus: '腹横肌 + 腹直肌 + 下背',
    color: 'fullbody',
    moves: [
      { name: '平板支撑',       sets: '3 × 45–60s', rest: '30s', image: 'plank.jpg' },
      { name: '死虫式',         sets: '3 × 12/侧', rest: '30s', image: 'core-workout.jpg' },
      { name: '卷腹',           sets: '3 × 20',    rest: '30s', image: 'crunch.jpg' },
      { name: '鸟狗式',         sets: '3 × 10/侧', rest: '30s', image: 'plank.jpg' },
      { name: '超人式',         sets: '3 × 12/侧', rest: '30s', image: 'core-workout.jpg' },
      { name: '侧平板',         sets: '2 × 30s/侧', rest: '30s', image: 'plank.jpg' }
    ],
    main: 'coreTabata',
    stretch: 'stretchAlt'
  }
};

/* ============================================================
   每日时间轴（分钟级）—— v3.0 基于新训练计划
   ============================================================ */
FIT.timeline = {
  pull: [
    { time: '06:50', type: 'exercise', text: '早：10 分钟肩康复热身 + 轻活动' },
    { time: '07:00', type: 'exercise', text: '晨起低冲击有氧 20 分钟（跟练）' },
    { time: '07:30', type: 'water',    text: '饮水 500ml' },
    { time: '08:00', type: 'food',     text: '早餐：鸡蛋 3 + 牛奶 250ml + 燕麦 30g' },
    { time: '09:00', type: 'move',     text: '小电动通勤' },
    { time: '11:30', type: 'water',    text: '饮水 500ml' },
    { time: '12:30', type: 'food',     text: '午餐：鸡胸 150g + 米饭 100g + 蔬菜' },
    { time: '15:30', type: 'water',    text: '饮水 500ml' },
    { time: '17:30', type: 'water',    text: '饮水 500ml' },
    { time: '20:30', type: 'exercise', text: '晚：拉日力量（哑铃划船 + 哑铃面拉）45 分钟' },
    { time: '21:20', type: 'food',     text: '晚餐：鸡胸 260g + 蔬菜 300g + 玉米 80g' },
    { time: '22:30', type: 'rest',     text: '泡沫轴背部 + 拉伸 15 分钟' },
    { time: '23:30', type: 'sleep',    text: '关灯睡觉（侧卧）' }
  ],
  push: [
    { time: '06:50', type: 'exercise', text: '早：肩康复热身 10 分钟（肩外旋 + 墙壁天使）' },
    { time: '07:30', type: 'water',    text: '饮水 500ml' },
    { time: '08:00', type: 'food',     text: '早餐：鸡蛋 3 + 牛奶 250ml + 燕麦 30g' },
    { time: '09:00', type: 'move',     text: '通勤' },
    { time: '12:30', type: 'food',     text: '午餐：鸡胸 150g + 米饭 100g + 蔬菜' },
    { time: '15:30', type: 'water',    text: '饮水 500ml' },
    { time: '20:30', type: 'exercise', text: '晚：推日训练（哑铃卧推 + 上斜推 + 侧平举）45 分钟' },
    { time: '21:20', type: 'food',     text: '晚餐：鸡胸 260g + 蔬菜 300g + 南瓜 200g' },
    { time: '22:30', type: 'rest',     text: '胸肩拉伸 + 肩外旋保护 10 分钟' },
    { time: '23:30', type: 'sleep',    text: '关灯睡觉' }
  ],
  leg: [
    { time: '06:50', type: 'exercise', text: '早：下肢动态热身 + 髋激活 10 分钟' },
    { time: '07:30', type: 'water',    text: '饮水 500ml' },
    { time: '08:00', type: 'food',     text: '早餐：鸡蛋 3 + 牛奶 250ml' },
    { time: '11:30', type: 'water',    text: '饮水 500ml' },
    { time: '12:30', type: 'food',     text: '午餐：牛肉 200g + 米饭 100g + 蔬菜' },
    { time: '15:30', type: 'water',    text: '饮水 500ml' },
    { time: '20:30', type: 'exercise', text: '晚：腿日训练（酒杯深蹲 + 分腿蹲 + 直腿硬拉）50 分钟' },
    { time: '21:25', type: 'food',     text: '晚餐：牛肉 260g + 蔬菜 300g + 红薯 100g' },
    { time: '22:30', type: 'rest',     text: '泡沫轴放松下肢 + 拉伸 15 分钟' },
    { time: '23:30', type: 'sleep',    text: '关灯睡觉' }
  ],
  cardio: [
    { time: '06:50', type: 'exercise', text: '早：低冲击有氧 25 分钟（跟练）' },
    { time: '07:30', type: 'water',    text: '饮水 500ml' },
    { time: '08:00', type: 'food',     text: '早餐：鸡蛋 3 + 牛奶 250ml' },
    { time: '09:00', type: 'move',     text: '通勤' },
    { time: '12:30', type: 'food',     text: '午餐：鸡胸 150g + 蔬菜' },
    { time: '18:00', type: 'exercise', text: '晚间：腹部核心 15 分钟（瑜伽垫上跟练）' },
    { time: '19:00', type: 'exercise', text: '餐后散步 30 分钟' },
    { time: '21:30', type: 'food',     text: '晚餐：鸡胸 260g + 蔬菜 300g + 玉米 80g' },
    { time: '22:30', type: 'rest',     text: '哑铃肩外旋 2×15' },
    { time: '23:30', type: 'sleep',    text: '关灯睡觉' }
  ],
  recovery: [
    { time: '07:30', type: 'rest',     text: '自然醒，不设闹钟' },
    { time: '08:00', type: 'food',     text: '早餐：鸡蛋 3 + 牛奶 250ml' },
    { time: '09:30', type: 'exercise', text: '10 分钟肩康复 + 20 分钟全身动态拉伸' },
    { time: '11:00', type: 'water',    text: '饮水 500ml' },
    { time: '14:00', type: 'exercise', text: '30–40 分钟慢速散步（公园/江边）' },
    { time: '17:00', type: 'water',    text: '饮水 500ml' },
    { time: '20:00', type: 'exercise', text: '泡沫轴 20 分钟 + 静态拉伸' },
    { time: '22:00', type: 'rest',     text: '电子宵禁 · 阅读' },
    { time: '23:00', type: 'sleep',    text: '提前入睡' }
  ],
  fullbody: [
    { time: '06:50', type: 'exercise', text: '早：跳绳新手跟练 10 分钟（间歇）' },
    { time: '07:30', type: 'water',    text: '饮水 500ml' },
    { time: '08:00', type: 'food',     text: '早餐：鸡蛋 3 + 牛奶 250ml + 燕麦 30g' },
    { time: '11:30', type: 'water',    text: '饮水 500ml' },
    { time: '12:30', type: 'food',     text: '午餐：鸡胸 150g + 米饭 100g + 蔬菜' },
    { time: '20:30', type: 'exercise', text: '晚：全身哑铃循环 30 分钟 + 核心 15 分钟' },
    { time: '21:20', type: 'food',     text: '晚餐：鸡胸/鱼虾 260g + 蔬菜 300g + 玉米 80g' },
    { time: '22:30', type: 'rest',     text: '放松拉伸 + 肩外旋保护' },
    { time: '23:30', type: 'sleep',    text: '关灯睡觉' }
  ]
};

/* ============================================================
   每周日程（周一到周日明确分配）—— 训练日跟练页面使用
   每天都包含：早晨 30 分钟训练 + 晚间训练
   ============================================================ */
FIT.weekly = [
  {
    day: '周一', dayKey: 'pull',
    title: '拉日 · 背 + 二头 + 后束',
    color: 'pull',
    morning: {
      title: '🌅 早晨 30 分钟：肩袖保护 + 背部激活',
      intro: '训练第一原则：肩袖保护先于一切。早晨以轻激活为主，不做冲击动作。',
      mainVideo: 'pullMorning',
      items: [
        '哑铃肩外旋 × 3 组 × 15 次（热身保护，必做）',
        '墙壁天使 × 3 组 × 10 次（胸椎活动，改善圆肩）',
        '轻哑铃俯身划船 × 3 组 × 12 次（背部唤醒）',
        '哑铃面拉 × 3 组 × 15 次（后束激活）',
        '轻哑铃弯举 × 2 组 × 12 次（二头肌预热）'
      ],
      warmupVideo: 'shoulderRehab'
    },
    evening: {
      title: '🌙 晚间主课：轻重量哑铃 45 分钟',
      intro: '主课训练：俯身划船 + 哑铃面拉 + 硬拉（轻重量）。新手哑铃建议 3-5kg，动作标准优先于重量。',
      mainVideo: 'pullWorkout',
      planKey: 'pull',
      theoryVideo: 'pullTheory'
    }
  },
  {
    day: '周二', dayKey: 'cardio',
    title: '有氧 + 核心日',
    color: 'cardio',
    morning: {
      title: '🌅 早晨 30 分钟：低冲击有氧（快步走）',
      intro: '快走是 BMI 28+ 人群最安全的有氧。膝盖仅承受 1.5× 体重，远低于跑步的 3-4×。',
      mainVideo: 'lowImpactBriskWalk',
      items: [
        '原地热身踏步 + 关节活动 × 5 分钟',
        '快步走（90-120 步/分）× 20-25 分钟',
        '核心轻激活 × 5 分钟（死虫式 2×10 + 卷腹 2×12）',
        '补水 500ml'
      ],
      warmupVideo: 'shoulderRehab'
    },
    evening: {
      title: '🌙 晚间核心训练 25 分钟',
      intro: '瑜伽垫上完成，全程零冲击。腹部发力保持腰椎贴地。',
      mainVideo: 'morningCore',
      planKey: 'cardio',
      theoryVideo: null
    }
  },
  {
    day: '周三', dayKey: 'push',
    title: '推日 · 胸 + 肩 + 三头',
    color: 'push',
    morning: {
      title: '🌅 早晨 30 分钟：胸肩激活',
      intro: '训练中最容易伤肩的是卧推和肩推。早晨激活是防伤关键。',
      mainVideo: 'pushMorning',
      items: [
        '哑铃肩外旋 × 3 组 × 15 次（热身保护，必做）',
        '墙壁天使 × 3 组 × 10 次（胸椎活动）',
        '轻哑铃环绕 × 3 组 × 10 次（肩袖稳定）',
        '轻哑铃前平举 × 3 组 × 12 次（前束激活）',
        '俯卧撑跪姿 × 2 组 × 8 次（胸肌预热，累了就停）'
      ],
      warmupVideo: 'shoulderWarmup'
    },
    evening: {
      title: '🌙 晚间主课：哑铃卧推 + 肩推 45 分钟',
      intro: '主课训练：哑铃卧推（瑜伽垫上）+ 上斜推 + 侧平举 + 俯身臂屈伸。手肘保持 45° 不贴地。',
      mainVideo: 'pushWorkout',
      planKey: 'push',
      theoryVideo: 'pushTheory'
    }
  },
  {
    day: '周四', dayKey: 'cardio',
    title: '有氧 + 核心日',
    color: 'cardio',
    morning: {
      title: '🌅 早晨 30 分钟：低冲击有氧',
      intro: '快步走 + 动态拉伸，不做跳跃类动作。',
      mainVideo: 'lowImpactBriskWalk',
      items: [
        '原地踏步 + 关节活动 × 5 分钟',
        '快步走（90-120 步/分）× 20-25 分钟',
        '核心轻激活 × 5 分钟（平板 2×30 秒 + 臀桥 2×15）',
        '补水 500ml'
      ],
      warmupVideo: 'shoulderRehab'
    },
    evening: {
      title: '🌙 晚间核心训练 25 分钟',
      intro: 'Tabata 节奏，零冲击动作。注意用腹部发力，避免借腰力。',
      mainVideo: 'coreTabata',
      planKey: 'cardio',
      theoryVideo: null
    }
  },
  {
    day: '周五', dayKey: 'leg',
    title: '腿日 · 腿 + 臀 + 小腿',
    color: 'leg',
    morning: {
      title: '🌅 早晨 30 分钟：下肢激活（保护膝盖）',
      intro: '大体重人群最容易伤膝盖，早晨以保护式激活为主，不做深蹲/跳跃。',
      mainVideo: 'legMorning',
      items: [
        '哑铃肩外旋 × 2 组 × 15 次（全身训练都要护肩）',
        '徒手髋外展 × 3 组 × 15 次（臀激活）',
        '徒手深蹲 × 3 组 × 15 次（找动作感觉）',
        '单腿硬拉（无哑铃）× 2 组 × 8 次/侧',
        '提踵 × 3 组 × 20 次（小腿热身）'
      ],
      warmupVideo: 'shoulderRehab'
    },
    evening: {
      title: '🌙 晚间主课：轻重量腿训 50 分钟',
      intro: '主课训练：哑铃酒杯深蹲 + 分腿蹲 + 直腿硬拉 + 单腿臀桥。新手哑铃建议 5-7.5kg。',
      mainVideo: 'legWorkout',
      planKey: 'leg',
      theoryVideo: 'legTheory'
    }
  },
  {
    day: '周六', dayKey: 'fullbody',
    title: '全身哑铃循环日',
    color: 'fullbody',
    morning: {
      title: '🌅 早晨 30 分钟：低冲击全身循环',
      intro: '去掉了跳绳（BMI 28+ 严禁跳跃类动作），替换为低冲击全身循环 + 靠墙静蹲。',
      mainVideo: 'lowImpactFullbody',
      items: [
        '原地踏步 + 关节活动 × 5 分钟',
        '低冲击全身有氧 × 20 分钟（跟视频，无跳跃）',
        '靠墙静蹲 × 3 组 × 30 秒',
        '动态拉伸 × 5 分钟',
        '补水 500ml'
      ],
      warmupVideo: 'shoulderRehab'
    },
    evening: {
      title: '🌙 晚间全身哑铃循环 40 分钟',
      intro: '全身循环动作：杯式深蹲 → 哑铃卧推 → 哑铃划船 → 罗马尼亚硬拉 → 核心，每组间休息 60 秒。',
      mainVideo: 'fullbodyDumbbell',
      planKey: 'fullbody',
      theoryVideo: null
    }
  },
  {
    day: '周日', dayKey: 'recovery',
    title: '纯恢复日 · 拉伸 + 散步',
    color: 'recovery',
    morning: {
      title: '🌅 早晨轻活动 30 分钟',
      intro: '恢复日重点放松肩袖和筋膜，不做任何高强度。让肌肉有 48 小时恢复窗口。',
      mainVideo: 'shoulderRehab',
      items: [
        '哑铃肩外旋跟练 × 10 分钟（跟视频）',
        '全身动态拉伸 × 15 分钟',
        '慢速散步 × 10 分钟（不追求速度，仅促进循环）'
      ],
      warmupVideo: 'shoulderRehab'
    },
    evening: {
      title: '🌙 晚间放松 30 分钟',
      intro: '泡沫轴 + 静态拉伸，重点放松：胸肌、背阔肌、股四头肌、腘绳肌、小腿腓肠肌。',
      mainVideo: 'foamRoller',
      planKey: 'recovery',
      theoryVideo: null
    }
  }
];

/* ============================================================
   新手安全提示（在训练跟练页面展示）
   ============================================================ */
FIT.safety = [
  '⚠️ 新手前 2 周：哑铃单手握持不超过 7.5KG，找动作感觉为主',
  '⚠️ 每次训练前必须做肩康复热身（弹力带肩外旋）',
  '⚠️ 大体重避免：标准俯卧撑、深蹲跳、高冲击跳绳',
  '✅ 哑铃卧推时：躺在瑜伽垫上，肘部与身体成 45°，不要完全外展',
  '✅ 如训练后关节疼痛超过 2 天，降重量或换动作',
  '✅ 目标心率：有氧 110–140，力量训练间休息时 < 100'
];

// ============ URL 工具 ============
FIT.bvUrl = function (bvid) {
  return 'https://player.bilibili.com/player.html?bvid=' + bvid + '&page=1&high_quality=1&autoplay=0';
};
FIT.bvLink = function (bvid) {
  return 'https://www.bilibili.com/video/' + bvid;
};

// ============ 天气 Emoji 映射 ============
function wxEmo(c) {
  if (c >= 200 && c < 300) return '⛈️';
  if (c >= 300 && c < 400) return '🌧️';
  if (c >= 500 && c < 600) return '🌧️';
  if (c >= 600 && c < 700) return '🌨️';
  if (c >= 700 && c < 800) return '🌫️';
  if (c === 801) return '🌤️';
  if (c > 801) return '☁️';
  return '☀️';
}

// ============ 天气获取（带 localStorage 缓存 30 min）============
function fetchWeather(callback) {
  var CACHE_KEY = FIT.weather.cacheKey;
  var CACHE_TTL = FIT.weather.cacheTTL;
  var cached;
  try { cached = JSON.parse(localStorage.getItem(CACHE_KEY) || 'null'); } catch (e) { cached = null; }

  if (cached && Date.now() - cached.ts < CACHE_TTL) {
    callback(cached.data, null);
    return;
  }

  fetch(FIT.weather.url)
    .then(function (r) { return r.json(); })
    .then(function (data) {
      try { localStorage.setItem(CACHE_KEY, JSON.stringify({ ts: Date.now(), data: data })); } catch (e) {}
      callback(data, null);
    })
    .catch(function (err) {
      if (cached) { callback(cached.data, null); }
      else { callback(null, err); }
    });
}

// ============ 从 wttr.in 响应中提取明日天气 ============
function extractTomorrow(d) {
  if (!d || !d.weather || !d.weather[1]) return null;
  var tw = d.weather[1];
  var hourly = tw.hourly || [];
  var mid = Math.floor(hourly.length / 2);
  var evRain = hourly.filter(function (h) {
    var hr = parseInt(h.time) / 100;
    return hr >= 17 && hr <= 20;
  }).some(function (h) { return parseInt(h.chanceofrain) > 30; });
  return {
    minTemp: tw.mintempC,
    maxTemp: tw.maxtempC,
    desc: hourly.length ? hourly[mid].weatherDesc[0].value : '',
    weatherCode: hourly.length ? parseInt(hourly[mid].weatherCode) : 0,
    evRain: evRain
  };
}

// 兼容：保持变量名
if (typeof window !== 'undefined') {
  window.FIT = FIT;
}
